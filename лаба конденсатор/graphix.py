import matplotlib.pyplot as plt
import numpy as np

with open('izmerenya.txt', 'r') as file:
    data = file.readlines()
    data = np.array([float(line) for line in data])
    
with open('settings.txt', 'r') as file1:
    settings = file1.readlines()
    settings = [float(line.split(':',1)[1]) for line in settings]

period = settings[0]/len(data)
t =np.array([i*period for i in range(len(data))])
vremazar= t[np.argmax(data)]
vremaraz=round(t[-1]-vremazar,2)
vremazar = round(vremazar, 2)


plt.plot(t,data, color = 'green', linestyle = '-', linewidth = 2, marker = 'o', markersize = 5, markerfacecolor = 'orange', markevery=5, label='Напряжение, В')
plt.title('Зависимость напряжения от времени', fontsize=14, loc = 'left',pad = 5, wrap = True)
plt.xlabel('Время, с', fontsize=12)
plt.ylabel('Напряжение, В', fontsize=12)
plt.xlim(t.min(), t.max()+1)
plt.ylim(data.min(),data.max()+0.1)
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.grid(which = 'major', linestyle='-', color ='gray')
plt.grid(which = 'minor', linestyle='--', color ='gray')
plt.text(t.max()-15, data.max()-1, f"время зарядки:{vremazar} c\nВремя разрядки:{vremaraz} с", bbox=dict(facecolor='white', edgecolor='black'), color = 'black', size = 10)
plt.legend(fontsize=12)
plt.savefig('график.svg')
plt.show()