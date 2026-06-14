#2

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
