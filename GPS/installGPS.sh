#! /bin/bash
# author NianBao
echo "if the Serial raspi-comfig disable,you follow below by script."
echo "******Raspberry_Pi3_GPS_UART*******"
echo "**********Install--ALL*************"

sudo apt-get install gpsd gpsd-clients cmake subversion build-essential -y
sudo apt-get install espeak freeglut3-dev imagemagick libdbus-1-dev libdbus-glib-1-dev -y
sudo apt-get install libdevil-dev libfontconfig1-dev libfreetype6-dev libfribidi-dev -y
sudo apt-get install libgarmin-dev libglc-dev libgps-dev libgtk2.0-dev libimlib2-dev -y
sudo apt-get install libpq-dev libqt4-dev libqtwebkit-dev librsvg2-bin libsdl-image1.2-dev -y
sudo apt-get install libspeechd-dev libxml2-dev ttf-liberation -y

echo "**********Install--FINISH*************"

echo "Write core_freq=250 and enable_uart=1 in sudo vim /boot/config.txt"

echo "Change in 'sudo vim /boot/cmdline.txt'"
echo "Change ' dwc_otg.lpm_enable=0  console=tty1 root=/dev/mmcblk0p7 rootfstype=ext4  elevator=deadline fsck.repair=yes rootwait'"

echo "RUN below 1234"
echo "1.sudo systemctl stop serial-getty@ttyS0.service"
echo "2.sudo systemctl disable serial-getty@ttyS0.service"
echo "3.sudo systemctl stop gpsd.socket"
echo "4.sudo systemctl disable gpsd.socket"

echo "reboot if you above finish"

echo "sudo killall gpsd if you used gpsd"
echo "start: sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock"

echo "choose channel cat /dev/ttyS0 or gpsmon /dev/ttyS0 or with sudo cgps -s"

