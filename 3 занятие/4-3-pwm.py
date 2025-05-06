import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
    p = GPIO.PWM(24, 1000)
    p.start(0)
    while True:
        D = int(input())
        p.start(D)
        print(f'{3.3*D/100:.2f}')

finally:
    GPIO.cleanup()