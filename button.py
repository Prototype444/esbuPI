import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.OUT)
speed=0.5

def Blink():
	while True:
		GPIO.output(3,True)
		time.sleep(speed)
		GPIO.output(3,False)
		time.sleep(speed)

t = Thread(target=Blink, args=())
t.start()

while True:
	GPIO.wait_for_edge(7, GPIO.FALLING)
	if speed == 0.5:
		speed=0.1
	elif speed == 0.1:
		speed=0.04
	else:
		speed=0.5
