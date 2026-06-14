#1
'''
from math import * #для тангенсов и прочего
for x in [-1,1]: #переменная
    a,b=-0.5,1.2 
    z=(2**-x)*atan(x+a)-(3**(-b*x))*cos(x+b)
    print(z)
'''
#2
'''
from math import * #для тангенсов и прочего
x=float(input('Введите х принадлежащий [0.5, 2]:'))
if (x<=2) and (x>=0.5):#проверка введенных значений
    def z(n): #сама функция
        a=-0.8
        if n>1: return sin((cos(n))**a)
        if n==1: return (tan(n))**a
        if n<1: return (a**2)*n
    print(z(x))
else:print('Я ЖЕ ПРОСИЛ ОТ 0.5 ВКЛЮЧАЯ ДО 2 ТОЖЕ ВКЛЮЧАЯ')#сообщение об ошибке
'''
#3

from math import * #для тангенсов и прочего
for a in [0.1,0.2,0.3]:
    dx=a #шаг
    for x in range(int(0.1*10),int((0.9+dx)*10),int(dx*10)):
        x=x/10
        def z(n):
            if 0.1<=n<=0.5: return (((sin(x))**2)+a**2)*exp(a*sin(x))
            if 0.5<=n<=0.9: return tan(x/4)
        print(z(x))

