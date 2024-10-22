import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.HIGH)
GPIO.output(20,GPIO.HIGH)
GPIO.output(12,GPIO.HIGH)
print ("green")
GPIO.output(21,GPIO.LOW)
time.sleep(5)
GPIO.output(21,GPIO.HIGH)
print ("yellow")
GPIO.output(21,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
time.sleep(1)
GPIO.output(21,GPIO.HIGH)
GPIO.output(12,GPIO.HIGH)
print ("red")
GPIO.output(12,GPIO.LOW)
time.sleep(4)
GPIO.output(12,GPIO.HIGH)
i = 0


