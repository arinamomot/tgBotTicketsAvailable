
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

from selenium import webdriver
import chromedriver_autoinstaller

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import schedule
import time
import telebot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')
bot = telebot.TeleBot(token=TOKEN)
my_id = os.getenv('MY_TELEGRAM_ID')
URL = os.getenv('MUSEUM_URL')
interval_seconds = int(os.getenv('CHECK_INTERVAL'))

# Function to extract available dates using Selenium WebDriver
def is_soldout():
    try:
      # Configure Chrome WebDriver
      chrome_options = webdriver.ChromeOptions()
      chrome_options.add_argument('--headless') # this is must
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
      chromedriver_autoinstaller.install()

      driver = webdriver.Chrome(options=chrome_options)

      # Load the webpage
      driver.get(URL)

      # Wait for dynamic content to load (adjust the sleep time as needed)
      time.sleep(10)

      parent_element = driver.find_element(By.CLASS_NAME, 'ui-datepicker-group-last')
      month_element = parent_element.find_element(By.CLASS_NAME, 'ui-datepicker-month')
      month = month_element.text.strip()
      if month.lower() == 'april':
          # Find the calendar table element
          calendar = parent_element.find_element(By.TAG_NAME, 'table')
          soldout = True
          for td in calendar.find_elements(By.TAG_NAME, 'td'):
            class_attr = td.get_attribute('class')
            if class_attr is not None:
              classes = td.get_attribute('class').split()
              if 'soldout' not in classes and 'ui-state-disabled' not in classes:
                  for a in td.find_elements(By.TAG_NAME, 'a'):
                      text = a.text.strip()
                      if (text == '1' or text == '2'):
                      # if (text == '7'):
                          soldout = False

      # Quit the WebDriver session
      driver.quit()

      return soldout
    except Exception as e:
        print(f"An error occurred during ChromeDriver setup: {e}")
        return None

def check_and_send():
    try:
        soldout = is_soldout()
        if not soldout:
            bot.send_message(my_id, "AVAILABLE!!!")
        # if soldout:
        #     bot.send_message(my_id, 'Still sold out')
    except Exception as e:
        bot.send_message(my_id, f"An error occurred: {e}")

# Schedule the task to run every hour
# schedule.every(10).seconds.do(check_and_send)
# schedule.every().hour.do(check_and_send)

# Start the bot
while True:
    check_and_send()
    # schedule.run_pending()
    time.sleep(interval_seconds)