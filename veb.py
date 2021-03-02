import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate
from sympy import *
def func (t):
    return (1-exp(-(t/211.5929)**1.9448))
sample=[]
f=open('nn.txt',"r")
for line in f:
    sample+=[float(line.strip('\n').replace(',', '.'))]
sample.sort() #расположение элементов выборки по возрастанию
xlist = sample
ylist = [func (x) for x in xlist]
x2 = []
y2 = []
y1 = 0
for x in sample:
    x2.extend([x,x])
    y2.append(y1)
    y1 += 1.0 / len(sample)
    y2.append(y1)
plt.hlines(y=1, xmin=540.448, xmax=560, color='m')
plt.title('График эмпирической функции распределения и гамма-распределения')
plt.ylabel('Fe, FГ')
plt.xlabel('t')
plt.grid(which='both')
plt.plot (xlist, ylist,label = u'Fw(t)')#вывод на экран графика FГ(t)
plt.plot(x2,y2, color='m', label = u'Fe(t)')#вывод на экран графика Fe(t);
plt.show()
