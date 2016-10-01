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
Motor_time_sleep=5

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

def Forward () : 
        print("F")
        GPIO.output(Motor_A_1, False)
        GPIO.output(Motor_A_2, True)
        GPIO.output(Motor_B_1, True)
        GPIO.output(Motor_B_2, False)
        time.sleep(Motor_time_sleep)
        
        
def Backward () :  
        print("B")
        GPIO.output(Motor_A_1, True)
        GPIO.output(Motor_A_2, False)
        GPIO.output(Motor_B_1, False)
        GPIO.output(Motor_B_2, True)
        time.sleep(Motor_time_sleep)
        
def Right () : 
        print("L")
        GPIO.output(Motor_A_1, True)
        GPIO.output(Motor_A_2, False)
        GPIO.output(Motor_B_1, True)
        GPIO.output(Motor_B_2, False)
        time.sleep(Motor_time_sleep)
        
def Left () : 
        print("L")
        GPIO.output(Motor_A_1, False)
        GPIO.output(Motor_A_2, True)
        GPIO.output(Motor_B_1, False)
        GPIO.output(Motor_B_2, True)
        time.sleep(Motor_time_sleep)

try:
  while True:
    Forward()
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

    distance_M = (stop_M - start_M) * 34000 / 2
    distance_L = (stop_L - start_L) * 34000 / 2
    distance_R = (stop_R - start_R) * 34000 / 2

    print "------L-------"
    print "{:.1f}".format(distance_L)
    print "------M-------"
    print "{:.1f}".format(distance_M)
    print "------R-------"
    print "{:.1f}".format(distance_R)
    
    if distance_L < 15:
        Backward();
    else:
        print ("P")

except KeyboardInterrupt:
 GPIO.cleanup()
