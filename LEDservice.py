import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)


while True:
    try:
        speed=int(os.environ['LEDSPEED'])
    except:
        speed=2
	GPIO.output(3,True)
	time.sleep(speed)
	GPIO.output(3,False)
	time.sleep(speed)
