"""
sudo apt-get update
sudo apt-get purge wolfram-engine
sudo apt-get purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove

sudo apt-get upgrade
sudo pip3 install -U pip
sudo apt-get install python-dev python-pip libfreetype6-dev libjpeg-dev build-essential

sudo -H pip3 install --upgrade luma.oled
sudo apt-get install i2c-tools
sudo pip3 install adafruit-pca9685
sudo pip3 install rpi-ws281x
sudo apt-get install mpu6050-raspberrypi
sudo apt-get install python3-smbus
sudo pip3 install flask
sudo pip3 install flask_cors
sudo pip3 install websockets

in file /boot/config.txt
change
#dtparam=i2c_arm=on
into
dtparam=i2c_arm=on
start_x=1

sudo pip3 install numpy
sudo pip3 install opencv-contrib-python=3.4.3.18
sudo apt-get install libqtgui4 libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqt4-test
sudo pip3 install imutils zmq pybase64 psutil

sudo git clone https://github.com/oblique/create_ap

cd /create_ap
sudo make install

sudo apt-get install util-linux procps hostapd iproute2 iw haveged dnsmasq

sudo touch /home/pi/startup.sh
in this file
#! /bin/sh
sudo python3 ./server/webServer.py
or
sudo python3 ./server/server.py

sudo chmod 777 /home/pi/startup.sh

in file /etc/rc.local
add this in the end of file
/home/pi/startup.sh

sudo touch /etc/modprobe.d/snd-blacklist.conf
in this file
blacklist snd_bcm2835

sudo reboot
"""