#10

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

