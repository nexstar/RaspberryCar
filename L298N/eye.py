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
Motor_time_sleep = 0.09
Ultrasound_time_sleep = 3
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

def Forward () : 
        print("F")
        GPIO.output(Motor_A_1, False)
        GPIO.output(Motor_A_2, True)
        GPIO.output(Motor_B_1, True)
        GPIO.output(Motor_B_2, False)
        time.sleep(Motor_time_sleep)
        Stop()


def Backward () :  
        print("B")
        GPIO.output(Motor_A_1, True)
        GPIO.output(Motor_A_2, False)
        GPIO.output(Motor_B_1, False)
        GPIO.output(Motor_B_2, True)
        time.sleep(Motor_time_sleep)
        Stop()
        


def Left () : 
        print("L")
        GPIO.output(Motor_A_1, True)
        GPIO.output(Motor_A_2, False)
        GPIO.output(Motor_B_1, True)
        GPIO.output(Motor_B_2, False)
        time.sleep(Motor_time_sleep)
        Stop()


def Right () : 
        print("R")
        GPIO.output(Motor_A_1, False)
        GPIO.output(Motor_A_2, True)
        GPIO.output(Motor_B_1, False)
        GPIO.output(Motor_B_2, True)
        time.sleep(Motor_time_sleep)
        Stop()


def Event_000():
        Forward ()
        time.sleep(0.5)
        Stop()


def Event_001():
        Left ()
        Forward()
        Right ()
        Forward()
        time.sleep(0.5)
        Stop()
 

def Event_010():
        from random import randint      
        Direction_Decision = randint(0,1)
        if (Direction_Decision == 0 ) :
                print("==000==")
                Event_001()
        elif(Direction_Decision == 1 ) :
                print("==111==")
                Event_100()


def Event_011():
        Backward ()
        Left ()
        Forward()
        Right ()
        Forward()
        time.sleep(0.5)
        Stop()
 

def Event_100():
        Right ()
        Forward()
        Left ()
        Forward()
        time.sleep(0.5)
        Stop()


def Event_101():
        Forward () 
        time.sleep(0.5)
        Stop()
 

def Event_110():
        Backward ()
        Right ()
        Forward()
        Left ()
        Forward()
        time.sleep(0.5)
        Stop()


def Event_111():
        Backward ()
        time.sleep(0.5)
        Stop()
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
                        Event_011()
                        ans = "011"
                elif distance_L <=Safe_value and distance_M >Safe_value and distance_R >Safe_value :
                        Event_100()
                        ans = "100"
                elif distance_L <=Safe_value and distance_M >Safe_value and distance_R <=Safe_value :
                        Event_101()
                        ans = "101"
                elif distance_L <=Safe_value and distance_M <=Safe_value and distance_R >Safe_value :
                        Event_110()
                        ans = "110"
                elif distance_L <=Safe_value and distance_M <=Safe_value and distance_R <=Safe_value :
                        Event_111()
                        ans = "111"
                print(ans,distance_L , distance_M , distance_R)
except KeyboardInterrupt:
 GPIO.cleanup()
