import os
speed=os.environ['LEDSPEED']

while True:
	GPIO.output(3,True)
	time.sleep(speed)
	GPIO.output(3,False)
	time.sleep(speed)
