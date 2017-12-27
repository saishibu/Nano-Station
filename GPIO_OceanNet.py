import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)


while (1):
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	print "high"
	time.sleep(72)
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
	print "low"
	time.sleep(72)