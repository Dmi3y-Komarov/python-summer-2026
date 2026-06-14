#3

from math import * #для тангенсов и прочего
for a in [0.1,0.2,0.3]:
    dx=a #шаг
    for x in range(int(0.1*10),int((0.9+dx)*10),int(dx*10)):
        x=x/10
        def z(n):
            if 0.1<=n<=0.5: return (((sin(x))**2)+a**2)*exp(a*sin(x))
            if 0.5<=n<=0.9: return tan(x/4)
        print(z(x))
