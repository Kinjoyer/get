import RPi.GPIO as GPIO
import time 

leds = [2,3,4,17,27,22,10,9]
sch = 0
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
time.sleep(0.2)
def queue(leds):
    for i in leds:
        GPIO.output(i,1)
        time.sleep(0.2)
        GPIO.output(i,0)
while sch < 3:
    sch += 1
    queue(leds)

GPIO.cleanup()