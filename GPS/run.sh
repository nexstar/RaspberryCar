#! /bin/bash

echo "sudo killall gpsd if you used gpsd"
sudo killall gpsd 
echo "start: sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock"
sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock
echo "choose channel cat /dev/ttyS0 or gpsmon /dev/ttyS0 or with sudo cgps -s"
sudo cgps -s
