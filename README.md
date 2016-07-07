## RaspberryCar
### Environment
raspberry pi2 B 
raspberry pi3 B
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


