#4

from math import * #для экспоненты
import sys
from functools import lru_cache #кусок из functools, отвечающий за кэш

sys.setrecursionlimit(10**6) #лимит рекурсии увеличили
lru_cache()#должно ускорить счёт при больших значениях 

def ex(n): #отвечает за часть 1/1!+1/2!+1/3!+1/4!...
    if n>=1:
        return ex(n-1)+1/factorial(n)
    else:
        return 0 #конец рекурсии

def exn(n):
    return ex(n)+1 #отвечает за часть 1 + ex(n)

try:
    x=int(input('Введите число: ')) #для ручной проверки
except:
    print('Ошибка: вы введи не число!')
else:

    #print (exn(1000)) #проверка

    if (exp(1)-exn(x))==0:
        print("Равны")

    elif (exp(1)-exn(x))>0:
        print("Самодельная экспонента меньше")

    else:
        print("Самодельная экспонента больше")

    #print (exp(1)-exn(x))#еще проверка

    m = {(abs(exp(1) - exn(t))) : t for t in range(1, 50)} #находим при каком n exp(1) максимально похоже на exn(n)

    M = min(m.keys())
    print (f"Самодельная экспонента максимально близка к exp(1) при n = {m[M]}. Разница между значениями составляет {M}")
