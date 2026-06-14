#7

s=list(input('Введите ЛЮБОЙ текст: '))
numbers='1','0','2','3','4','5','6','7','8','9'
b=[bool()]
for i in range(len(s)):
    if s[i] in numbers:s[i]=True
    else:s[i]=False
    b[0]=b[0] or s[i]
print(b)

