sum1=0
sum2=0
sum3=0
sum4=0
N=50 #объём выборки
f=open('nn.txt',"r") #обращение к выборке
for line in f:
    sum1 += float(line.strip('\n').replace(',', '.'))
    sum2 += (float(line.strip('\n').replace(',', '.')))**2
    sum3 += (float(line.strip('\n').replace(',', '.')))**3
    sum4 += (float(line.strip('\n').replace(',', '.')))**4
#вычисление начальных моментов
m1=(sum1)/N
m2=(sum2)/N
m3=(sum3)/N
m4=(sum4)/N
print('Начальные моменты:','m1 =', m1, 'm2 =', m2,'m3 =', m3,'m4 =', m4) #вывод на экран
Sum22 = 0
Sum23 = 0
Sum24 = 0
T=m1
#вычисление центральных смещённых моментов, D, σ, Sk, Ex по начальным моментам
mu2=m2-m1**2
mu3=m3-3*m1*m2+2*m1**3
mu4=m4-4*m1*m3+6*m1**2*m2-3*m1**4
print('Центральные смещённые моменты по начальным моментам:','mu2 = D =', mu2, 'mu3 =', mu3,'mu4 =', mu4) #вывод на экран
sko=mu2**0.5 #вычисление смещённого среднеквадратичного отклонения
sks=mu3/sko**3 #вычисление смещённого коэффициента асимметрии
exs=(mu4/sko**4)-3 #вычисление смещённого коэффициента островершинности
print('По начальным моментам:','sko = σ =', sko,'sks =', sks, 'exs =', exs) #вывод на экран
f=open('nn.txt',"r")
for line in f:
    Sum22 += (float(line.strip('\n').replace(',', '.')) - T) ** 2
    Sum23 += (float(line.strip('\n').replace(',', '.')) - T)**3
    Sum24 += (float(line.strip('\n').replace(',', '.')) - T) ** 4
#вычисление центральных смещённых моментов, D, σ, Sk, Ex по выборке
Mu2=Sum22/N
Mu3=Sum23/N
Mu4=Sum24/N
print('Центральные смещённые моменты по выборке:','Mu2 = D =', Mu2, 'Mu3 =', Mu3,'Mu4 =', Mu4) #вывод на экран
Sko=Mu2**0.5 #вычисление смещённого среднеквадратичного отклонения
Sks=Mu3/Sko**3 #вычисление смещённого коэффициента асимметрии
Exs=(Mu4/Sko**4)-3 #вычисление смещённого коэффициента островершинности
print('По выборке:','Sko = σ =', Sko,'Sks =', Sks, 'Exs =', Exs) #вывод на экран
# вычисление центральных несмещённых моментов
Mu2n=Sum22/(N-1)
Mu3n = (N**2/((N-1)*(N-2)))*Mu3
Mu4n = ((N*(N**2-2*N+3)*Mu4)-(3*N*(2*N-3)*Mu2**2))/((N-1)*(N-2)*(N-3))
Skon = Mu2n**0.5 #вычисление несмещённого среднеквадратичного отклонения
Skn=((N*(N-1))**0.5/(N-2))*Sks #вычисление несмещённого коэффициента асимметрии
Exn = ((N-1)/((N-2)*(N-3)))*((N+1)*Exs+6) #вычисление несмещённого коэффициента островершинности
print('Центральные несмещённые моменты:','Mu2n = Dn =', Mu2n, 'Mu3n =', Mu3n,'Mu4n =', Mu4n,'Skon = σn= ', Skon,'Skn =', Skn, 'Exn =', Exn) #вывод на экран

#Построение графика Fe(t)
import matplotlib.pyplot as plt
sample=[]
f=open('nn.txt',"r")
for line in f:
    sample+=[float(line.strip('\n').replace(',', '.'))]
sample.sort() #расположение элементов выборки по возрастанию
x2 = []
y2 = []
y = 0
for x in sample:
    x2.extend([x,x])
    y2.append(y)
    y += 1.0 / len(sample)
    y2.append(y)
plt.hlines(y=1, xmin=540.448, xmax=560, color='m')
plt.title('Эмпирическая функция распределения')
plt.ylabel('Fe')
plt.xlabel('t')
plt.plot(x2,y2, color='m')
plt.grid(which='both')
plt.show()

#Критерий "стареющего" распределения
import math
M=[]
k=0
M.extend([m1,m2,m3,m4])
for element in M:
    M[k]=element/math.factorial(k+1) #расчёт Mk
    print('M', k + 1, '=', M[k], end='  ')
    k+=1
print()
# проверка критерия "стареющего" распределения
r1=M[2]*M[0]-M[1]**2
r2=M[3]*M[1]-M[2]**2
print('r1=', r1, 'r2=',r2)

