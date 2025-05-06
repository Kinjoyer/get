import RPi.GPIO as GPIO
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def chislbin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def raschnapr(binel):
    if binel == chislbin(0):
        return 0
    else:        
        return sum(3.3/(2**(i+1)) for i,c in enumerate(binel) if c == '1')
try:
    while True:
        try: 
            v = input()
            if v == 'q':
                break
            else: 
                v = int(v)
                GPIO.output(dac, chislbin(v))
                print(f'{round(raschnapr(bin(v)[2:].zfill(8)),3)} V')
        except RuntimeError:
            print('число выходит за пределы допустимого диапазона от 0 до 255')
        except ValueError:
            try:
                int(v)
                if int(v)<0:
                    print('Введено отрицательное число')
            except ValueError:
                try:
                    float(v)
                    print('Введено не целое число')
                except ValueError:
                    print('Введено не число')


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
