import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac =[8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT,initial = GPIO.HIGH)
def chislbin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def adc(dac,comp):
    for i in range(256):
        bini = chislbin(i)
        GPIO.output(dac, bini)
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            return i
    return 255
        
try:
    while True:
        dv = adc(dac,comp)
        v = dv*(3.3/256)
        print(dv,round(v,2))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()


