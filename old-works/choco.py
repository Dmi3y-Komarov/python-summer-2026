#4
'''
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
'''
#5
'''
def f(n): #выдает числа Фибоначчи
    if n==0 or n==1: return 1
    else: return f(n-1)+f(n-2)
F,n=0,0#переменная хранящая сумму и типо счетчик
while f(n)<=1000:F+=f(n);n+=1#Суммирует числа Фибоначчи, пока они не начнут превышать 1000
print(F)
'''
#6
'''
MN=int(input('Введите порядок матрицы: '))#порядок квадратной матрицы(m=n) для решения общего случая
if MN<=1:print('Это не матрица');quit()#проверка того, что ввел пользователь
t=[]#массив(блокнот, не знаю), содержащий строки матрицы
counter,mn=0,MN#счетчик и счетчик, можно было 1, сейчас лень менять
while mn>0:#построчный ввод произвольной матрицы
    counter+=1#счетчик
    print(f'Введите {counter} строку матрицы из {MN}, в строке должно быть {MN} элементов, в качестве разделителя используйте пробел')#сообщение пользователю
    elements=list(map(int, input().split()))
    if len(elements)!=MN:print('Неверное число элементов');quit()#проверка введенных данных
    t+=[elements]#добавление строки в массив
    mn+=-1#счетчик
#print(t)#проверка
counter,true=0,0#счетчик, считающий порядок элемента в строке или строку, и хранилище совпадающих строк
while counter<=(MN-2):#цикл сравнения строк и столбцев
    s,S,c='','',0#да
    while c<=(MN-1):#цикл создания рядов посимвольно
        s+=str(t[counter][c])
        S+=str(t[c][counter])
        c+=1
    #print(s,S)
    if s==S: true+=1#сравнение строки и столбца. запись результата
    counter+=1
if true==MN-1:print('Данная матрица симметрична относительно главной диагонали')#вывод
else:print('Данная матрица не симметрична относительно главной диагонали')
'''
#6Oleg
'''
s=input('Введите 24 числа: ').split()

if len(s)!=24:print('Error');quit()
s.reverse()
print(f'{s[:6]}\n{s[6:12]}\n{s[12:18]}\n{s[18:]}')
'''
#2 iz 3
'''
x1,x2,y1,y2=1, 2, 3, 4
def MAx(z,v,o):
    if z>v and z>o:return z
    if v>z and v>o:return v
    if o>v and o>z:return o
def MIn(z,v):
    if z<v:return z

    else:return v
print(MAx(x1,y1,x2)*MIn(y1-5,y2+4))
'''
#7 iz 20
'''
s=input('Введите любой текст на руском: ')
#print(type(s))
glas='а','е','ё','и','о','у','ы','э','ю','я'
t=[]
for i in range(len(s)):
    a=s[i]
    if a in glas:t+=[i]
s=s.replace('а','А').replace('е','Е').replace('ё','Ё').replace('и','И').replace('о','О').replace('у','У').replace('ы','Ы').replace('э','Э').replace('ю','Ю').replace('я','Я')
print(s)
'''
#4 iz 1
'''
k=int(input('Введите ваш возраст: '))
god='1'
godA='2','3','4'
let='5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'
if str(k%100) in let:print('Вам '+str(k)+' лет')
elif str(k%10) in let:print('Вам '+str(k)+' лет')
elif str(k%10) in god:print('Вам '+str(k)+' год')
elif str(k%10) in godA:print('Вам '+str(k)+' года')
'''
#7
'''
s=list(input('Введите ЛЮБОЙ текст: '))
numbers='1','0','2','3','4','5','6','7','8','9'
b=[bool()]
for i in range(len(s)):
    if s[i] in numbers:s[i]=True
    else:s[i]=False
    b[0]=b[0] or s[i]
print(b)
'''
#8
'''
m0=input('Введите 20 чисел в любом порядке, в качестве разделителя используйте пробел: ').split()
if len(m0)!=20:print('А по условию надо 20 чисел');quit()
m=[int(x) for x in m0]
#print(m)
m.sort()
#print(m)
t=[]
for i in range(len(m)):
    if m[i]%2==0:t+=[i]
c=0
for i in t:
    del m[i-c]
    c+=1
print(m)
'''
#9
'''
k=input('Введите любое время(часы:минуты): ').split(':')
if int(k[0])>=24 or int(k[0])<0:print('Часы только от 0 до 23');quit('Ошибка пользователя')
if int(k[1])>=60 or int(k[1])<0:print('МИнуты только от 0 до 59');quit('Ошибка пользователя')
cas=['1','21']
for i in range(10,40,10):
    cas+=[str(int(cas[1])+i)]
casA=['2','3','4','22','23','24']
for i in range(10,40,10):
    casA+=[str(int(casA[3])+i)]
    casA+=[str(int(casA[4])+i)]
    casA+=[str(int(casA[5])+i)]
casOV=['0','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
for i in range(10,50,10):
    casOV+=[str(int(casOV[6])+i)]
    casOV+=[str(int(casOV[11])+i)]
    casOV+=[str(int(casOV[12])+i)]
    casOV+=[str(int(casOV[13])+i)]
    casOV+=[str(int(casOV[14])+i)]
    casOV+=[str(int(casOV[15])+i)]  
if k[0] in casOV:
    if k[1] in casOV: print('Время(веденное вами): '+k[0]+' часов '+k[1]+' минут.')
    elif k[1] in cas: print('Время(веденное вами): '+k[0]+' часов '+k[1]+' минута.')
    elif k[1] in casA: print('Время(веденное вами): '+k[0]+' часов '+k[1]+' минуты.')
elif k[0] in cas:
    if k[1] in casOV: print('Время(веденное вами): '+k[0]+' час '+k[1]+' минут.')
    elif k[1] in cas: print('Время(веденное вами): '+k[0]+' час '+k[1]+' минута.')
    elif k[1] in casA: print('Время(веденное вами): '+k[0]+' час '+k[1]+' минуты.')
elif k[0] in casA:
    if k[1] in casOV: print('Время(веденное вами): '+k[0]+' часа '+k[1]+' минут.')
    elif k[1] in cas: print('Время(веденное вами): '+k[0]+' часа '+k[1]+' минута.')
    elif k[1] in casA: print('Время(веденное вами): '+k[0]+' часа '+k[1]+' минуты.')
'''
#10
'''
from math import *#для округления в большую сторону до int
mn=int(input('Введите порядок матрицы, минимум 3: '))
if mn<3:print('Error');quit()#проверка данных
matrix=[]#будущая матрица
chet=mn%2==0#можно было сразу в иф
matrix+=['1 '*(mn-1)+str(mn)]#первая строка
#print(matrix)
if chet:#алгоритм немного отличается из-за четности
    for i in range(1,int(mn/2)):#создаем первую половину, не считая первую строку
        matrix+=['0 '*i+str(i+1)+' '+'1 '*(mn-4-(2*(i-1)))+str(mn-i)+' '+'0 '*i]#строки до половины имеют такой вид
        #print(matrix,i)
    matrix+=[matrix[-1]]#первая строка после половины повторяет предыдущую
    #print(matrix,i)
    Rmatrix=[]#второй кусок матрицы, который будет .reverse()
    Rmatrix+=['1 '+'0 '*(mn-2)+str(mn)]#последняя строка матрицы
    for i in range(1,int(mn/2-1)):#вторая половина матрицы, без первой и последней строк
        Rmatrix+=['0 '*i+str(i+1)+' '+'0 '*(mn-4-(2*(i-1)))+str(mn-i)+' '+'0 '*i]
    Rmatrix.reverse()    
    matrix+=Rmatrix
    #print(matrix)
else:
    for i in range(1,int(mn//2)):
        matrix+=['0 '*i+str(i+1)+' '+'1 '*(mn-4-(2*(i-1)))+str(mn-i)+' '+'0 '*i]
        #print(matrix,i)
    matrix+=['0 '*(mn//2)+str(ceil(mn/2))+' '+'0 '*(mn//2)]#отличие из-за четности
    #print(matrix,i)
    Rmatrix=[]
    Rmatrix+=['1 '+'0 '*(mn-2)+str(mn)]
    for i in range(1,int(mn//2)):
        Rmatrix+=['0 '*i+str(i+1)+' '+'0 '*(mn-4-(2*(i-1)))+str(mn-i)+' '+'0 '*i]
    Rmatrix.reverse()    
    matrix+=Rmatrix
for i in range(mn):print(matrix[i])
'''
#11
'''
import openpyxl as o

book=o.open('11 Банк.xlsx',read_only=True)
List=book.active
#print(int((List[2][2].value).year))
for i in range(1,List.max_row+1):
    if List[i][1].value=='Омск' and (1970<int((List[i][2].value).year)<1979):print(List[i][0].value)
'''






#4 iz 11
'''
from math import *
n=100
for a in [0.5,1.0]:
    dx=(a*n)/2
    for x in range(1*n,(4+1)*n,int(dx)):
        x=x/n
        if 1<=x<=2.5:z=a*((x*a)**(3/2));print(z,x,' 1')
        elif 2.5<x<=4:(a/2)*(exp(x/a)+exp(-x/a));print(z,x,' 2')
'''
#5 iz 3
'''
from math import *
def F1(x):
    return 4*exp(-abs(x))-1
def F2(x):
    return cos(x)
k=100
a=-1
b=5
n=15
dx=(b-a)/n
c=0
print(f'a  b n  F1(x) F2(x)')
for x in range(a*k,(b+1)*k,int(dx*k)):
    c+=1
    if c>15 and x<=b:break
    x=x/k
    print(f'{a} {b} {n} {F1(x):.3f}  {F2(x):.3f} ')
'''





















