#Метод максимального правдоподобия для распределения Вейбулла
import math
N=50 #количество элементов выборки
sample=[]
f=open('nn.txt',"r")
for line in f:
    sample+=[float(line.strip('\n').replace(',', '.'))]
from scipy.optimize import fsolve # библиотека для решения нелинейных уравнений
def f(a):
    sum1 = 0
    sum2=0
    sum3 = 0
    f1=N/a
    for t in sample:
        sum1 += (t**a)*math.log(t)
        sum2+=t**a
        sum3 += math.log(t)
    f2=N*(sum1/sum2)
    return f1-f2+sum3
a = fsolve(f, 1) #начальное приближение решения уравнения a0=1
a=float(a[0])
print('Расчёт методом максимального правдоподобия для распределения Вейбулла:')
print('a =', a)#вывод на экран параметра a
sum4=0
for t in sample:
    sum4 += t ** a
b=(sum4/N)**(1/a)#вывод на экран параметра b
print('b =', b)
#Расчёт σ, Sk, Ex для аппроксимирующего распределения Вейбулла
from sympy import * #библиотека для символьных вычислений
D1=(b**2)*(gamma(1+2/a)-(gamma(1+1/a))**2)
Sko=D1**0.5
Sk=((2*((gamma(1+1/a))**3))-(3*gamma(1+1/a))*(gamma(1+2/a))+(gamma(1+3/a)))/((gamma(1+2/a))-((gamma(1+1/a))**2))**(3/2)
Ex=((gamma(1+4/a)-4*gamma(1+3/a)*gamma(1+1/a)+6*gamma(1+2/a)*(gamma(1+1/a))**2-3*(gamma(1+1/a))**4)/(gamma(1+2/a)-(gamma(1+1/a))**2)**2)-3
print('Sko =', Sko, 'Sk =', Sk, 'Ex =', Ex)

#Построение графиков Fe(t) и Fw(t)
import matplotlib.pyplot as plt #графическая библиотека
def func1 (t):
    return (1-exp(-(t/b)**a))
sample.sort() #расположение элементов выборки по возрастанию
xlist1 = sample
ylist1 = [func1 (x) for x in xlist1]
x2 = []
y2 = []
y1 = 0
for x in sample:
    x2.extend([x,x])
    y2.append(y1)
    y1 += 1.0 / len(sample)
    y2.append(y1)
plt.hlines(y=1, xmin=354.223, xmax=380, color='m')
plt.title('График эмпирической функции распределения и распределения Вейбулла')
plt.ylabel('Fe, Fw')
plt.xlabel('t')
plt.grid(which='both')
plt.plot(x2,y2, color='m', label = u'Fe(t)')#вывод на экран графика Fe(t)
plt.plot (xlist1, ylist1,label = u'Fw(t)')#вывод на экран графика Fw(t)
plt.legend ()
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
    yabs=abs(y2y[i]-ylist1[i])
    yy.append(yabs)
plt.title('График y(t)')
plt.ylabel('y')
plt.xlabel('t')
plt.plot(yx,yy, color='g') #вывод на экран графика y(t)
plt.grid(which='both')
plt.show()
D2=max(yy) #нахождение параметра D
N=50
l2=D2*N**0.5 #нахождение параметра 𝜆
print('D =',D2, 'l =', l2) #вывод на экран параметров D, 𝜆
