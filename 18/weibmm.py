# Метод моментов для распределения Вейбулла
T=227.68662400000002 #среднее время наработки до отказа
D=3393.62612652227 #дисперсия несмещённая
print('Расчёт методом моментов для распределения Вейбулла:')
Ya=(D/T**2)+1
print('Ya =', Ya )
import math #библитека математических функций и констант
from sympy import * #библиотека для символьных вычислений
a = symbols('a')
a1=1+1/a
a2=1+2/a
Q1=1+(1/12)*a1**(-1)+(1/288)*a1**(-2)-(139/51840)*a1**(-3)-(571/2488320)*a1**(-4)
G1=exp(-a1)*a1**(a1-0.5)*((2*math.pi)**0.5)*Q1
Q2=1+(1/12)*a2**(-1)+(1/288)*a2**(-2)-(139/51840)*a2**(-3)-(571/2488320)*a2**(-4)
G2=exp(-a2)*a2**(a2-0.5)*((2*math.pi)**0.5)*Q2
d=G2/(G1**2)
#print('d =',d)
from scipy.optimize import fsolve # библиотека для решения нелинейных уравнений
def f(a):
   return Ya-0.398942280401433*(1 + 1/a)**(-1.0 - 2/a)*(1 + 2/a)**(0.5 + 2/a)*(1 + 0.0833333333333333/(1 + 2/a) + 0.00347222222222222/(1 + 2/a)**2 - 0.00268132716049383/(1 + 2/a)**3 - 0.000229472093621399/(1 + 2/a)**4)*math.exp(-1 - 2/a)*math.exp(2 + 2/a)/(1 + 0.0833333333333333/(1 + 1/a) + 0.00347222222222222/(1 + 1/a)**2 - 0.00268132716049383/(1 + 1/a)**3 - 0.000229472093621399/(1 + 1/a)**4)**2
a = fsolve(f, 0.5) #начальное приближение решения уравнения a0=0.5
a=float(a[0])
print('a=',a)#вывод на экран параметра a
b=T/gamma(1+1/a)
print('b =',b) #вывод на экран параметра b

#Построение графиков Fe(t) и Fw(t)
import matplotlib.pyplot as plt #графическая библиотека
def func1 (t):
    return (1-exp(-(t/b)**a))
sample=[]
f=open('nn.txt',"r")
for line in f:
    sample+=[float(line.strip('\n').replace(',', '.'))]
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
plt.hlines(y=1, xmin=362.5173, xmax=382, color='m')
plt.title('График эмпирической функции распределения и распределения Вейбулла')
plt.ylabel('Fe, Fw')
plt.xlabel('t')
plt.grid(which='both')
plt.plot(x2,y2, color='m', label = u'Fe(t)')#вывод на экран графика Fe(t)
plt.plot (xlist1, ylist1,label = u'Fw(t)')#вывод на экран графика Fw(t)
plt.legend ()
plt.show()

#Расчёт σ, Sk, Ex для аппроксимирующего распределения Вейбулла
D1=(b**2)*(gamma(1+2/a)-(gamma(1+1/a))**2)
Sko=D1**0.5
Sk=((2*((gamma(1+1/a))**3))-(3*gamma(1+1/a))*(gamma(1+2/a))+(gamma(1+3/a)))/((gamma(1+2/a))-((gamma(1+1/a))**2))**(3/2)
Ex=((gamma(1+4/a)-4*gamma(1+3/a)*gamma(1+1/a)+6*gamma(1+2/a)*(gamma(1+1/a))**2-3*(gamma(1+1/a))**4)/(gamma(1+2/a)-(gamma(1+1/a))**2)**2)-3
print('Sko =', Sko, 'Sk =', Sk, 'Ex =', Ex)

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
