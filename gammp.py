#Метод максимального правдоподобия для гамма-распределения
import math
N=50 #количество элементов выборки
T=187.63408999999996 #среднее время наработки до отказа
sample=[]
f=open('nn.txt',"r")
for line in f:
    sample+=[float(line.strip('\n').replace(',', '.'))]
summ=0
for t in sample:
    summ+=math.log(t/T)
S=summ/N
print('Расчёт методом максимального правдоподобия для гамма-распределения:')
print('S =', S)

from scipy.optimize import fsolve # библиотека для решения нелинейных уравнений
def f(a):
    Q = 1 + (1 / (12 * (a ** 2))) + (1 / (288 * (a ** 2))) - (139 / (51840 * (a ** 3))) - (571 / (2488320 * (a ** 4)))
    G = S-((-1 + ((a - 0.5) / a) + (-(1 / (12 * (a ** 2))) - (2 / (288 * (a ** 3))) + (3 * 139 / 51840 * (a ** 4)) + (571 * 4 / (2488320 * (a ** 5))))) / Q)
    return G
a = fsolve(f, 0.5) #начальное приближение решения уравнения a0=0.5
a=float(a[0])
print('a =', a)#вывод на экран параметра a
l=a/T
print('𝜆 =', l) #вывод на экран параметра 𝜆
# Расчёт σ, Sk, Ex для аппроксимирующего гамма-распределения
Sko=(a**0.5)/l
Sk=2/(a**0.5)
Ex=6/a
print('Sko =', Sko,'Sk =', Sk, 'Ex =', Ex)

#Построение графиков FГ(t) и Fe(t)
from sympy import * #подключение библиотеки символьной математики sympy
t = symbols('t')
K=(l**a)/gamma(a)
dd=K*(t**(a-1))*exp(-l*t)
ff=integrate(dd,t,manual=True) #вычисление FГ(t)
print('FГ(t) =', ff,'+ С' )
C= 1.00125384601698*uppergamma(1.99702943604777, 0)#постоянная интегрирования
print('С =', C)
print('FГ(t) =', ff, '+', C) #вывод на экран FГ(t)
import matplotlib.pyplot as plt #графическая библиотека
sample=[]
f=open('nn.txt',"r")
for line in f:
    sample+=[float(line.strip('\n').replace(',', '.'))]
sample.sort() #расположение элементов выборки по возрастанию
def func (x):
    return (-1.00125384601698*uppergamma(1.99702943604777, 0.0106432122011931*x) + 0.999999999999997)
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
plt.plot(x2,y2, color='m', label = u'Fe(t)')#вывод на экран графика Fe(t)
plt.grid(which='both')
plt.plot (xlist, ylist, label = u'FГ(t)')#вывод на экран графика FГ(t)
plt.legend()
plt.show()

#Построение графика y(t)
y2y=([y2[i] for i in range(len(y2)-1) if y2[i] != y2[i+1]])
x2y=([x2[i] for i in range(len(x2)-1) if x2[i] != x2[i+1]])
x2y.append(x2[-1])
yx=[]
yy=[]
yabs=0
for i in range(len(sample)):
    yx.append(sample[i])
    yabs=abs(y2y[i]-ylist[i])
    yy.append(yabs)
plt.title('График y(t)')
plt.ylabel('y')
plt.xlabel('t')
plt.plot(yx,yy, color='g')#вывод на экран графика y(t)
plt.grid(which='both')
plt.show()
D1=max(yy) #нахождение параметра D
N=50
l1=D1*N**0.5 #нахождение параметра 𝜆
print('D =', D1,'l =', l1) #вывод на экран параметров D, 𝜆