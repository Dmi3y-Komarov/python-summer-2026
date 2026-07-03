#3

from math import * #для тангенсов и прочего


def z(n, b):
    if 0.1<=n<=0.5: return (((sin(n))**2)+b**2)*exp(b*sin(n))
    if 0.5<=n<=0.9: return tan(n/4)

for a in [0.1,0.2,0.3]:
    dx=a #шаг
    for x in range(int(0.1*10),int((0.9+dx)*10),int(dx*10)):
        x=x/10
        print(z(x, a))
