from sympy import *
import pylab
import math
from sympy.abc import t
from sympy import init_printing
#g=gamma(3.47765)
a = 3.477648189048853
l = 0.018534202335241178
t = symbols('t')
#a= symbols('a')
#l = symbols('l')
K=(l**a)/gamma(a)
dd=K*(t**(a-1))*exp(-l*t)
#dd=K*(t ** (a - 1)) * exp(-l * t)
ff=integrate(dd,t,manual=True)
C=0.308387311935103*uppergamma(3.47764818904885, 0)
print(ff)
#print(K)
#print(g)
print(C)

#f = Function('f')
#x = symbols('x')
#diffeq =Eq(f(x).diff(x),(l ** a) * (x ** (a - 1)) * (exp(-l * x)) /g)
#print(diffeq)
#print(dsolve(diffeq, f(x)))

import numpy as np
import matplotlib.pyplot as plt
sample=[]
f=open('nn.txt',"r")
for line in f:
    sample+=[float(line.strip('\n').replace(',', '.'))]
sample.sort()

def func (x):
    return (-0.308387311935103*uppergamma(3.47764818904885, 0.0185342023352412*x)+1)
xlist = sample
ylist = [func (x) for x in xlist]
# !!! Нарисуем одномерный график
#pylab.plot (xlist, ylist)

# !!! Покажем окно с нарисованным графиком
#pylab.show()

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
plt.ylabel('Fe, F')
plt.xlabel('t')
plt.plot(x2,y2, color='m')
plt.grid(which='both')
plt.plot (xlist, ylist)
plt.show()