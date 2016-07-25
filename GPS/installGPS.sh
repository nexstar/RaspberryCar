#! /bin/bash
# author NianBao
echo "***Install--ALL***"
sudo apt-get update
sudo apt-get install python-smbus python-serial -y
sudo apt-get install minicom -y

echo "***Install--FINISH***"
echo "check raspi-config，enable serial"
echo "device:" 
dmesg | grep tty

