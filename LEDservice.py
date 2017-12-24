import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
speed=os.environ['LEDSPEED']

while True:
	GPIO.output(3,True)
	time.sleep(speed)
	GPIO.output(3,False)
	time.sleep(speed)
