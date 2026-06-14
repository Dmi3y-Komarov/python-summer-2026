#8

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
