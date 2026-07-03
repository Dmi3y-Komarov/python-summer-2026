#2 from 3

x1,x2,y1,y2=1, 2, 3, 4

def MAX(z,v,o):
    return z if z>v and z>o else ( v if v>o else o)
def MIn(z,v):
    return z if z<v else v
print(MAX(x1,y1,x2)*MIn(y1-5,y2+4))
