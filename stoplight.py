import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
print ("green")
GPIO.output(21,GPIO.HIGH)
time.sleep(5)
GPIO.output(21,GPIO.LOW)
print ("yellow")
GPIO.output(20,GPIO.HIGH)
time.sleep(1)
GPIO.output(20,GPIO.LOW)
print ("red")
GPIO.output(12,GPIO.HIGH)
time.sleep(4)
GPIO.output(12,GPIO.LOW)
i = 0


