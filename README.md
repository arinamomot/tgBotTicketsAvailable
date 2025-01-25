# Ticket Availability Checker Bot

A bot designed to automatically check and notify user about ticket availability for ... museum.

## Features

- Automated ticket availability monitoring
- Real-time notifications when tickets become available
- Customizable checking intervals


## For Google Colab
```bash
%%shell
sudo apt -y update
sudo apt install -y wget curl unzip
wget http://archive.ubuntu.com/ubuntu/pool/main/libu/libu2f-host/libu2f-udev_1.1.4-1_all.deb
dpkg -i libu2f-udev_1.1.4-1_all.deb
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb

wget -N https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/118.0.5993.70/linux64/chromedriver-linux64.zip -P /tmp/
unzip -o /tmp/chromedriver-linux64.zip -d /tmp/
chmod +x /tmp/chromedriver-linux64/chromedriver
mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver
pip install selenium chromedriver_autoinstaller
```

```bash
!pip install selenium
!pip install telebot
!pip install schedule
!apt install chromium-chromedriver
!pip install webdriver_manager
```
