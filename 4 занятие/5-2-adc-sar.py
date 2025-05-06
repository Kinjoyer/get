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
    otv = 0
    totv = 128

    
    GPIO.output(dac, chislbin(128))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        otv =totv

    totv=otv+64
    GPIO.output(dac, chislbin(totv))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        otv =totv
    
    totv=otv+32
    GPIO.output(dac, chislbin(totv))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        otv =totv
    
    totv=otv+16
    GPIO.output(dac, chislbin(totv))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        otv =totv
    
    totv=otv+8
    GPIO.output(dac, chislbin(totv))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        otv =totv

    totv=otv+4
    GPIO.output(dac, chislbin(totv))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        otv =totv
    
    totv=otv+2
    GPIO.output(dac, chislbin(totv))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        otv =totv

    totv=otv+1
    GPIO.output(dac, chislbin(totv))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        otv =totv
    return(otv)
try:
    while True:
        dv = adc(dac,comp)
        v = dv*(3.3/256)
        print(dv,round(v,2))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
