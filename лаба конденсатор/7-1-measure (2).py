import RPi.GPIO as GPIO # блок в котором настраивается малинка
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac =[8,11,7,1,0,5,12,6]
leds =[2,3,4,17,27,22,10,9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)


def adc(dac,comp): # функция для определения уровня напряжения на конденсаторе 
    totv = 128

    GPIO.output(dac, [int(element) for element in bin(totv)[2:].zfill(8)])
    time.sleep(0.004)
    if GPIO.input(comp) == 0:
        totv +=64
    else:
        totv -=64

    GPIO.output(dac, [int(element) for element in bin(totv)[2:].zfill(8)])
    time.sleep(0.004)
    if GPIO.input(comp) == 0:
        totv +=32
    else:
        totv -=32
    GPIO.output(dac, [int(element) for element in bin(totv)[2:].zfill(8)])
    time.sleep(0.004)
    if GPIO.input(comp) == 0:
        totv +=16
    else:
        totv -=16
    
    GPIO.output(dac, [int(element) for element in bin(totv)[2:].zfill(8)])
    time.sleep(0.004)
    if GPIO.input(comp) == 0:
        totv +=8
    else:
        totv -=8
        
    GPIO.output(dac, [int(element) for element in bin(totv)[2:].zfill(8)])
    time.sleep(0.004)
    if GPIO.input(comp) == 0:
        totv +=4
    else:
        totv -=4
    
    GPIO.output(dac, [int(element) for element in bin(totv)[2:].zfill(8)])
    time.sleep(0.004)
    if GPIO.input(comp) == 0:
        totv +=2
    else:
        totv -=2

    GPIO.output(dac, [int(element) for element in bin(totv)[2:].zfill(8)])
    time.sleep(0.004)
    if GPIO.input(comp) == 0:
        totv +=1
    else:
        totv -=1
    return(totv)



try: 
    ism = [] # блок прведения измерений
    dv = 0
    print('началась зарядка конденсатора')
    starttime=time.time()
    GPIO.output(troyka, 1)
    while dv<241:
        dv = adc(dac,comp)
        ism.append(dv)
    print('началась разрядка конденсатора')
    GPIO.output(troyka, 0)
    while dv>31:
        dv = adc(dac,comp)
        ism.append(dv)
    endtime = time.time()
    exptime = endtime-starttime # блок обработки результатов
    for i in range(len(ism)):
        ism[i] *= (3.3/256)
    period = exptime/len(ism)
    x =[i*period for i in range(len(ism))]

    ismstr = [str(i) for i in ism]

    with open('izmerenya.txt', 'w') as f:
        f.write('\n'.join(ismstr))
        
    with open('settings.txt', 'w') as f:
        f.write(f'частота дискретизации:{len(ism)/exptime} \n шаг квантования:{(max(ism)-min(ism))/2**(len(ism))}')
    
    print(f'время эксперимента:{exptime} \n период измерений:{period} \n средняя частота дискретизации:{len(ism)/exptime}')

    plt.plot(x,ism) 
    plt.show()
finally:
    GPIO.output(dac, 0) # блок сброса настроек и завершения работы
    GPIO.output(leds, 0)
    GPIO.cleanup()
    