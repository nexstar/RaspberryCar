import RPi.GPIO as  gpio
from random import randint
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
# Initial Code


"""------------Pin_Setup Global Variables-------------"""
Motor_A = 11
Motor_B = 13 
Motor_A_1 = 15
Motor_A_2 = 16
Motor_B_1 = 19
Motor_B_2 = 21
Motor_time_sleep = 1
gpio_TRIGGER = 32
gpio_ECHO_L = 36 
gpio_ECHO_M = 38 
gpio_ECHO_R = 40 
Ultrasound_time_sleep = 0.2
distance_L = 0
distance_M = 0
distance_R = 0
Safe_value = 5
Dangerous_values = 50
"""------------Pin_Setup Global Variables-------------"""

def Initial_Motor_Code () :
	"""-------------------------"""
	gpio.setmode(gpio.BOARD)
	gpio.setup(Motor_A, gpio.OUT)#is Motor Ctrl  Point		
	gpio.setup(Motor_B, gpio.OUT) 
	gpio.setup(Motor_A_1, gpio.OUT)#is A Motor	
	gpio.setup(Motor_A_2, gpio.OUT) 
	gpio.setup(Motor_B_1, gpio.OUT)#is B Motor	
	gpio.setup(Motor_B_2, gpio.OUT)  
	gpio.output(Motor_A, True)		
	gpio.output(Motor_B, True)
	"""-------------------------"""
	
def Initial_Ultrasound_Code () :	
	"""-------------------------"""
	gpio.setup(gpio_TRIGGER, gpio.OUT)
	gpio.setup(gpio_ECHO_L, gpio.IN)
	gpio.setup(gpio_ECHO_M, gpio.IN)
	gpio.setup(gpio_ECHO_R, gpio.IN)
	"""-------------------------"""

def distance(gpio_ECHO):
    gpio.output(gpio_TRIGGER, True)# set Trigger High
    time.sleep(0.0001)# set Trigger after 0.1ms low
    gpio.output(gpio_TRIGGER, False)
    startTime = time.time()
    endTime = time.time()
    while gpio.input(gpio_ECHO) == 0:# store start time
		startTime = time.time()		
    while gpio.input(gpio_ECHO) == 1: # store arrival
		endTime = time.time()	
    distance = ((endTime - startTime) * 34300) / 2 # multiply with speed of sound (34300 cm/s)	
    return ( distance ) # and division by two
"""-------------------------"""

"""-------------------------"""	
def Forward () : 
	gpio.output(Motor_A_1,  False)
	gpio.output(Motor_A_2, True)
	gpio.output(Motor_B_1, True)
	gpio.output(Motor_B_2,  False)
	print("Forward")
	time.sleep(Motor_time_sleep)
	
def Backward () :  
	gpio.output(Motor_A_1, True)
	gpio.output(Motor_A_2, False)
	gpio.output(Motor_B_1, False)
	gpio.output(Motor_B_2, True)
	print("Backward")
	time.sleep(Motor_time_sleep)
	
def Right () : 
	gpio.output(Motor_A_1, True)
	gpio.output(Motor_A_2,  False)
	gpio.output(Motor_B_1, True)
	gpio.output(Motor_B_2,  False)
	print("Right")
	time.sleep(Motor_time_sleep)
	
def Left () : 
	gpio.output(Motor_A_1,  False)
	gpio.output(Motor_A_2, True)
	gpio.output(Motor_B_1, False)
	gpio.output(Motor_B_2,  True)
	print("Left")
	time.sleep(Motor_time_sleep)
	
"""-------------------------"""
def Event_000():
	Forward ()
	
def Event_001():
	Left ()
	Forward()
	Right ()
	Forward()
	
def Event_010():
	from random import randint	
	Direction_Decision = randint(0,1)
	if (Direction_Decision == 0 ) :
		Event_001()
	elif(Direction_Decision == 1 ) :
		Event_100()
		
def Event_011():
	Backward ()
	Left ()
	Forward()
	Right ()
	Forward()
	
def Event_100():
	Right ()
	Forward()
	Left ()
	Forward()
	
def Event_101():
	Forward () 
	
def Event_110():
	Backward ()
	Right ()
	Forward()
	Left ()
	Forward()
	
def Event_111():
	Backward ()
	
"""-------------------------"""
def Car_Main():
	ans = "---"
	while True:  
		distance_L = distance(gpio_ECHO_L)
		time.sleep(0.2)
		distance_M = distance(gpio_ECHO_M)
		time.sleep(0.2)
		distance_R = distance(gpio_ECHO_R)
		time.sleep(0.2)	
		
		if distance_L >Safe_value and distance_M >Safe_value and distance_R >Safe_value :
			Event_000()
			ans = 000
		elif distance_L >Safe_value and distance_M >Safe_value and distance_R <=Safe_value :
			Event_001()
			ans = 001
		elif distance_L >Safe_value and distance_M <=Safe_value and distance_R >Safe_value :
			Event_010()
			ans = 010
		elif distance_L >Safe_value and distance_M <=Safe_value and distance_R <=Safe_value :
			Event_011()
			ans = 011
		elif distance_L <=Safe_value and distance_M >Safe_value and distance_R >Safe_value :
			Event_100()
			ans = 100
		elif distance_L <=Safe_value and distance_M >Safe_value and distance_R <=Safe_value :
			Event_101()
			ans = 101
		elif distance_L <=Safe_value and distance_M <=Safe_value and distance_R >Safe_value :
			Event_110()
			ans = 110
		elif distance_L <=Safe_value and distance_M <=Safe_value and distance_R <=Safe_value :
			Event_111()
			ans = 111		
		time.sleep( Ultrasound_time_sleep )
		print( ans,distance_L , distance_M , distance_R)

		
Initial_Motor_Code () 
Initial_Ultrasound_Code ()	
while True:  
	Car_Main()	

