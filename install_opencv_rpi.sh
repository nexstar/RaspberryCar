#! /bin/bash
#update package
sudo apt-get update
sudo apt-get dist-upgrade -y

#install opencvlib-dev
sudo apt-get install libopencv-dev -y

#build and compiler
sudo apt-get install build-essential gcc cmake pkg-config git -y

#python tools
sudo apt-get install python python-dev python-numpy -y

#x-windows
sudo apt-get install libgtk2.0-dev -y

#audio and video install tools
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev -y

#install picture
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev libjasper-dev -y 

#install camera insterface IEEE1394
sudo apt-get install libdc1394-22-dev -y

#wget TBB source and setting
wget https://www.threadingbuildingblocks.org/sites/default/files/software_releases/source/tbb44_20151115oss_src.tgz
tar zxvf tbb44_20151115oss_src.tgz
cd tbb44_20151115oss
make tbb CXXFLAGS="-DTBB_USE_GCC_BUILTINS=1 -D__TBB_64BIT_ATOMICS=0"
cd build
cd linux_armv7_gcc_cc4.9.2_libc2.19_kernel4.1.13_release
source tbbvars.sh

#git opencv
mkdir ~/opencv && cd opencv
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.0.0
mkdir build && cd build
cmake -DWITH_TBB:BOOL=TRUE -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..

make -j4
#install
sudo make install
#update cmd
sudo ldconfig

#check opencv version
pkg-config --modversion opencv










