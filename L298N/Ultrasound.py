import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO_TRIGGER = 32
GPIO_ECHO_L = 36 
GPIO_ECHO_M = 38 
GPIO_ECHO_R = 40 
"""-------------------------"""
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO_L, GPIO.IN)
GPIO.setup(GPIO_ECHO_M, GPIO.IN)
GPIO.setup(GPIO_ECHO_R, GPIO.IN)
"""-------------------------"""
def distance():
    GPIO.output(GPIO_TRIGGER, True)# set Trigger High
    time.sleep(0.00001)# set Trigger after 0.1ms low
    GPIO.output(GPIO_TRIGGER, False) 

    startTime_L = time.time()
    startTime_M = time.time()
    startTime_R = time.time()

    endTime_L = time.time()
    endTime_M = time.time()
    endTime_R = time.time()

    while GPIO.input(GPIO_ECHO_L) == 0:# store start time
        startTime_L = time.time()	
    while GPIO.input(GPIO_ECHO_M) == 0:
        startTime_M = time.time()	
    while GPIO.input(GPIO_ECHO_R) == 0:
        startTime_R = time.time()		
    while GPIO.input(GPIO_ECHO_L) == 1: # store arrival
        endTime_L = time.time()
    while GPIO.input(GPIO_ECHO_M) == 1:
        endTime_M = time.time()
    while GPIO.input(GPIO_ECHO_R) == 1:
        endTime_R = time.time()
    TimeElapsed_L = endTime_L - startTime_L # elapsed time
    TimeElapsed_M = endTime_M - startTime_M
    TimeElapsed_R = endTime_R - startTime_R
    distance_L = (TimeElapsed_L * 34300) / 2 # multiply with speed of sound (34300 cm/s)
    distance_M = (TimeElapsed_M * 34300) / 2
    distance_R = (TimeElapsed_R * 34300) / 2
    return ( distance_L , distance_M ,  distance_R  ) # and division by two

while True:    
    print("cm_L=%f/cm_M=%f/cm_R=%f" % distance())
    time.sleep(0.5)
