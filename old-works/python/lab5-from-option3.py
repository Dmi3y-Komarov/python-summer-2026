#5 iz 3

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

