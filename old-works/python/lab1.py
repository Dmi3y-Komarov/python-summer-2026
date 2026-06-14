#1

from math import * #для тангенсов и прочего
for x in [-1,1]: #переменная
    a,b=-0.5,1.2 
    z=(2**-x)*atan(x+a)-(3**(-b*x))*cos(x+b)
    print(z)
