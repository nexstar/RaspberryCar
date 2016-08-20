#! /bin/bash
# author NianBao
echo "***Install--ALL***"
sudo apt-get update
sudo apt-get install python-smbus python-serial -y
sudo apt-get install gpsd gpsd-clients python-gps -y
echo "***Install--ALL***"
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket
sudo systemctl enable gpsd.socket
sudo systemctl start gpsd.socket

echo "***Install--FINISH***"
echo "check raspi-config，enable serial"
echo "device:" 
#can check your uart
dmesg | grep tty
#rpi2
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
#rpi3
#sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock
