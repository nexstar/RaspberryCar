#!/usr/bin/env python
# author: NianBao
import RPi.GPIO as gpio
import time

# Initial Code

gpio.cleanup()

time.sleep(20)

gpio.setmode(gpio.BOARD)

gpio.setup(11, gpio.OUT)		
gpio.setup(13, gpio.OUT)	
# 7 , 12 is Motor Ctrl  Point 


gpio.setup(15, gpio.OUT)	
gpio.setup(16, gpio.OUT)	
#13 , 15 is A Motor 


gpio.setup(19, gpio.OUT)	
gpio.setup(21, gpio.OUT)	
#16 , 18 is B Motor 

gpio.output(11, True)		
gpio.output(13, True)

print "Forward"
gpio.output(15,False)
gpio.output(16,True)
gpio.output(19,True)
gpio.output(21,False)
time.sleep(100)

gpio.cleanup()

"""
 True
False
"""

