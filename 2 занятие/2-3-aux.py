import RPi.GPIO as GPIO
import time

leds = [2,3,4,17,27,22,10,9]
aux = [21,20,26,16,19,25,23,24]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

def cycle(leds,aux):
    for i in range(len(leds)):
        GPIO.output(leds[i],GPIO.input(aux[i]))
        
while True:
    cycle(leds,aux)
    time.sleep(0.1)
