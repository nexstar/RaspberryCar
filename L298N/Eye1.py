#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)

TRIG_M = 8
ECHO_L = 12
ECHO_M = 7
ECHO_R = 11

Motor_A=15
Motor_B=16
Motor_A_1=19
Motor_A_2=21
Motor_B_1=23
Motor_B_2=24
Safe_value = 50

GPIO.setup(TRIG_M, GPIO.OUT)
GPIO.setup(ECHO_L, GPIO.IN)
GPIO.setup(ECHO_M, GPIO.IN)
GPIO.setup(ECHO_R, GPIO.IN)


###########################
GPIO.setup(Motor_A, GPIO.OUT)
GPIO.setup(Motor_B, GPIO.OUT) 
GPIO.setup(Motor_A_1, GPIO.OUT)#is A Motor      
GPIO.setup(Motor_A_2, GPIO.OUT) 
GPIO.setup(Motor_B_1, GPIO.OUT)#is B Motor      
GPIO.setup(Motor_B_2, GPIO.OUT)

GPIO.output(Motor_A, True)
GPIO.output(Motor_B, True)

def Stop():
        print("STOP")
        GPIO.output(Motor_A_1, False)
        GPIO.output(Motor_A_2, False)
        GPIO.output(Motor_B_1, False)
        GPIO.output(Motor_B_2, False)

def Forward(Motor_time_sleep): 
        print("F")
        GPIO.output(Motor_A_1, False)
        GPIO.output(Motor_A_2, True)
        GPIO.output(Motor_B_1, True)
        GPIO.output(Motor_B_2, False)
        time.sleep(Motor_time_sleep)
        Stop()

def Backward(Motor_time_sleep):  
        print("B")
        GPIO.output(Motor_A_1, True)
        GPIO.output(Motor_A_2, False)
        GPIO.output(Motor_B_1, False)
        GPIO.output(Motor_B_2, True)
        time.sleep(Motor_time_sleep)
        Stop()

def Left(Motor_time_sleep): 
        print("L")
        GPIO.output(Motor_A_1, True)
        GPIO.output(Motor_A_2, False)
        GPIO.output(Motor_B_1, True)
        GPIO.output(Motor_B_2, False)
        time.sleep(Motor_time_sleep)
        Stop()


def Right(Motor_time_sleep): 
        print("R")
        GPIO.output(Motor_A_1, False)
        GPIO.output(Motor_A_2, True)
        GPIO.output(Motor_B_1, False)
        GPIO.output(Motor_B_2, True)
        time.sleep(Motor_time_sleep)
        Stop()

EndTime=0.01

def Event_000():##直
        Forward(0.09)
        time.sleep(EndTime)
        print("直")
        Stop()

def Event_111():##後
        Backward(0.09)
        time.sleep(EndTime)
        print("後")
        Stop()

def Event_001():##左直右直 只有右邊有擋住所以幅度不用很大
        Backward(0.07)
        Left(0.12)
        Forward(0.09)
        Right(0.08)
        Forward(0.1)
        time.sleep(EndTime)
        print("左直右直")
        Stop()
 
def Event_100():## 後右直左直
        Backward(0.07)
        Right(0.12)
        Forward(0.09)
        Left(0.08)
        Forward(0.1)
        time.sleep(EndTime)
        print("後右直左直")
        Stop()

def Event_010():##
        from random import randint      
        Direction_Decision = randint(0,1)
        if (Direction_Decision == 0 ) :
                print("==000==")
                Event_001()
        elif(Direction_Decision == 1 ) :
                print("==111==")
                Event_100()

"""-------------------------"""
try:
    while True:    
                GPIO.output(TRIG_M, 0)
                time.sleep(1)
                GPIO.output(TRIG_M, 1)
                time.sleep(0.1)
                GPIO.output(TRIG_M, 0)
                
                start_L= time.time()
                start_M = time.time()
                start_R = time.time()
                
                while GPIO.input(ECHO_M) == 0:
                  start_M = time.time()
                while GPIO.input(ECHO_M) == 1:
                  stop_M = time.time()
                
                
                while GPIO.input(ECHO_L) == 0:
                  start_L = time.time()
                while GPIO.input(ECHO_L) == 1:
                  stop_L = time.time()
                

                while GPIO.input(ECHO_R) == 0:
                  start_R = time.time()
                while GPIO.input(ECHO_R) == 1:
                  stop_R = time.time()
                
                distance_L = (stop_L - start_L) * 34000 / 2
                distance_M = (stop_M - start_M) * 34000 / 2
                distance_R = (stop_R - start_R) * 34000 / 2

                ans = "----"
                if distance_L >Safe_value and distance_M >Safe_value and distance_R >Safe_value :
                        Event_000()
                        ans = "000"
                elif distance_L >Safe_value and distance_M >Safe_value and distance_R <=Safe_value :
                        Event_001()
                        ans = "001"
                elif distance_L >Safe_value and distance_M <=Safe_value and distance_R >Safe_value :
                        Event_010()
                        ans = "010"
                elif distance_L >Safe_value and distance_M <=Safe_value and distance_R <=Safe_value :
                        Event_001() ## 取消011 宣告
                        ans = "!001"
                elif distance_L <=Safe_value and distance_M >Safe_value and distance_R >Safe_value :
                        Event_100()
                        ans = "100"
                elif distance_L <=Safe_value and distance_M >Safe_value and distance_R <=Safe_value :
                        Event_111()
                        Event_000()## 取消101宣告
                        ans = "!000"
                elif distance_L <=Safe_value and distance_M <=Safe_value and distance_R >Safe_value :
                        Event_100() ## 取消110 宣告
                        ans = "!100"
                elif distance_L <=Safe_value and distance_M <=Safe_value and distance_R <=Safe_value :
                        Event_111()
                        ans = "111"
                print(ans,distance_L , distance_M , distance_R)
except KeyboardInterrupt:
 GPIO.cleanup()
