#!/usr/bin/env python
# author: NianBao
import RPi.GPIO as gpio
import time

Motor_A=15
Motor_B=16
Motor_A_1=19
Motor_A_2=21
Motor_B_1=23
Motor_B_2=24
Motor_time_sleep=5

gpio.setmode(gpio.BOARD)
gpio.setup(Motor_A, gpio.OUT)#is Motor Ctrl  Point              
gpio.setup(Motor_B, gpio.OUT) 
gpio.setup(Motor_A_1, gpio.OUT)#is A Motor      
gpio.setup(Motor_A_2, gpio.OUT) 
gpio.setup(Motor_B_1, gpio.OUT)#is B Motor      
gpio.setup(Motor_B_2, gpio.OUT) 




gpio.output(Motor_A, True)
gpio.output(Motor_B, True)


def Forward () : 
        print("F")
        gpio.output(Motor_A_1, False)
        gpio.output(Motor_A_2, True)
        gpio.output(Motor_B_1, True)
        gpio.output(Motor_B_2, False)
        time.sleep(Motor_time_sleep)
        
        
def Backward () :  
        print("B")
        gpio.output(Motor_A_1, True)
        gpio.output(Motor_A_2, False)
        gpio.output(Motor_B_1, False)
        gpio.output(Motor_B_2, True)
        time.sleep(Motor_time_sleep)
        
def Right () : 
        print("L")
        gpio.output(Motor_A_1, True)
        gpio.output(Motor_A_2, False)
        gpio.output(Motor_B_1, True)
        gpio.output(Motor_B_2, False)
        time.sleep(Motor_time_sleep)
        
def Left () : 
        print("L")
        gpio.output(Motor_A_1, False)
        gpio.output(Motor_A_2, True)
        gpio.output(Motor_B_1, False)
        gpio.output(Motor_B_2, True)
        time.sleep(Motor_time_sleep)
try:
    while True:
        Forward()
        Right()
        Left()
        Backward()
except KeyboardInterrupt:
    gpio.cleanup()

