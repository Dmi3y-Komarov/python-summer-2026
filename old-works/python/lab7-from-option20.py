#7 iz 20

s=input('Введите любой текст на руском: ')
#print(type(s))
glas='а','е','ё','и','о','у','ы','э','ю','я'
t=[]
for i in range(len(s)):
    a=s[i]
    if a in glas:t+=[i]
s=s.replace('а','А').replace('е','Е').replace('ё','Ё').replace('и','И').replace('о','О').replace('у','У').replace('ы','Ы').replace('э','Э').replace('ю','Ю').replace('я','Я')
print(s)

