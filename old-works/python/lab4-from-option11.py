#4 iz 11

from math import *
n=100
for a in [0.5,1.0]:
    dx=(a*n)/2
    for x in range(1*n,(4+1)*n,int(dx)):
        x=x/n
        if 1<=x<=2.5:z=a*((x*a)**(3/2));print(z,x,' 1')
        elif 2.5<x<=4:(a/2)*(exp(x/a)+exp(-x/a));print(z,x,' 2')

