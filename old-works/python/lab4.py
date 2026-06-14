#4

from math import * #для экспоненты
import sys
sys.setrecursionlimit(10**6)#лимит рекурсии увеличили
from functools import lru_cache#кусок из functools, отвечающий за кэш
lru_cache()#должно ускорить счёт при больших значениях 
x=int(input())#для ручной проверки
def ex(n):#отвечает за часть 1/1!+1/2!+1/3!+1/4!...
    if n>=1:return ex(n-1)+1/factorial(n)
    else:return 0#конец рекурсии
def exn(n):return ex(n)+1#отвечает за часть 1 + ex(n)
#print (exn(1000)) #проверка

if (exp(1)-exn(x))==0: print("Равны")
elif (exp(1)-exn(x))>0:print("Самодельная экспонента меньше")
else: print("Самодельная экспонента больше")
#print (exp(1)-exn(x))#еще проверка

m=[]
for t in range(1,100):m+=[(abs(exp(1)-exn(t)),t)]#находим при каком n exp(1) максимально похоже на exn(n)
M=min(m)
print (f"самодельная экспонента максимально близка к exp(1) при n={M[-1]}")
