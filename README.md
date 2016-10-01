## RaspberryCar
### Environment
#### Hardware:
Raspberry pi2 B <br />
Raspberry pi3 B
#### Software:
OS:Lubuntu 15.10

### Install Ubuntu
Ref:
https://hackpad.com/ep/pad/static/CqbXLbtxEKg
### Opencv
```sh
$ git clone https://github.com/nexstar/RaspberryCar.git
$ cd RaspberryCar/opencv 
$ sudo chmod a+x install_opencv_rpi.sh
$./install_opencv_rpi.sh
```
compiler .cpp
```cpp
$ cd ~/opencv/opencv/samples/cpp
$ g++ facedetect.cpp -o facedetect `pkg-config --libs opencv` 
$./facedetect
```
compiler python
``` .py
$ cd ~/opencv/opencv/samples/python2
$ sudo pip install imutils
$ cp RaspberryCar/opencv/face_detect.py .
$ python face_detect.py
```
Set wifi ap for pi3
wifi ap and wifi one from two
``` wifi
$sudo apt-get install iw -y
$iw list //check wifi device whether AP function
$ifconfig //check wifi device name
$sudo vi /etc/network/interfaces
auto wlan0
iface wlan0 inet static 
    address 192.168.10.1
    netmask 255.255.255.0
$sudo ifdown wlan0
$sudo ifup wlan0
$ifconfig //check wlan0 ip whether success
#DHCP Server
$sudo apt-get -y install dnsmasq
$sudo vi /etc/dnsmasq.conf
interface=wlan0
dhcp-range=192.168.10.2,192.168.10.10,12h 
//ip range can't be use and need same class c ，12h=every 12hour change ip
$sudo systemctl restart dnsmasq
#hostapd
$sudo apt-get install hostapd
$sudo vi  /etc/hostapd/hostapd.conf
interface=wlan0
driver=nl80211
ssid=RPi-Wifi
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=password
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
$sudo vi etc/default/hostapd
DAEMON_CONF="/etc/hostapd/hostapd.conf"
$sudo hostapd -dd /etc/hostapd/hostapd.conf
$sudo update-rc.d hostapd defaults //set auto start, in every boot
$reboot

Ref
http://blog.itist.tw/2016/03/using-raspberry-pi-3-as-wifi-ap-with-raspbian-jessie.html
http://blog.yam.com/cistychang/article/61517499
http://chaoyunotebook.blogspot.tw/2015/10/raspberry-pi-wifi-ap.html

```

