#2 from 3

x1,x2,y1,y2=1, 2, 3, 4
def MAx(z,v,o):
    if z>v and z>o:return z
    if v>z and v>o:return v
    if o>v and o>z:return o
def MIn(z,v):
    if z<v:return z

    else:return v
print(MAx(x1,y1,x2)*MIn(y1-5,y2+4))
