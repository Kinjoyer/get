import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(19, GPIO.OUT)

if GPIO.input(25) == 1:
    GPIO.output(19, 1)
else:
    GPIO.output(19, 0)