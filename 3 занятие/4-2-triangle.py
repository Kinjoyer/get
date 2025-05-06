import time
import RPi.GPIO as GPIO
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def chislbin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    T = int(input())
    while True: 
        for i in range(1,256):
            GPIO.output(dac,chislbin(i))
            time.sleep(T/512)
            if i == 255:
                for i in range(254,-1,-1):
                    GPIO.output(dac,chislbin(i))
                    time.sleep(T/512)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()