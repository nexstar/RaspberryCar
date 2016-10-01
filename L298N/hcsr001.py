import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)

TRIG_M = 8


ECHO_L = 12
ECHO_M = 7
ECHO_R = 11

GPIO.setup(TRIG_M, GPIO.OUT)

GPIO.setup(ECHO_L, GPIO.IN)
GPIO.setup(ECHO_M, GPIO.IN)
GPIO.setup(ECHO_R, GPIO.IN)

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

    distance_M = (stop_M - start_M) * 34000 / 2
    distance_L = (stop_L - start_L) * 34000 / 2
    distance_R = (stop_R - start_R) * 34000 / 2

    print "------L-------"
    print "{:.1f}".format(distance_L)
    print "------M-------"
    print "{:.1f}".format(distance_M)
    print "------R-------"
    print "{:.1f}".format(distance_R)


except KeyboardInterrupt:
 GPIO.cleanup()
