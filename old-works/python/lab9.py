#9

k=input('Введите любое время(часы:минуты): ').split(':')
if int(k[0])>=24 or int(k[0])<0:print('Часы только от 0 до 23');quit('Ошибка пользователя')
if int(k[1])>=60 or int(k[1])<0:print('МИнуты только от 0 до 59');quit('Ошибка пользователя')
cas=['1','21']
for i in range(10,40,10):
    cas+=[str(int(cas[1])+i)]
casA=['2','3','4','22','23','24']
for i in range(10,40,10):
    casA+=[str(int(casA[3])+i)]
    casA+=[str(int(casA[4])+i)]
    casA+=[str(int(casA[5])+i)]
casOV=['0','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
for i in range(10,50,10):
    casOV+=[str(int(casOV[6])+i)]
    casOV+=[str(int(casOV[11])+i)]
    casOV+=[str(int(casOV[12])+i)]
    casOV+=[str(int(casOV[13])+i)]
    casOV+=[str(int(casOV[14])+i)]
    casOV+=[str(int(casOV[15])+i)]  
if k[0] in casOV:
    if k[1] in casOV: print('Время(веденное вами): '+k[0]+' часов '+k[1]+' минут.')
    elif k[1] in cas: print('Время(веденное вами): '+k[0]+' часов '+k[1]+' минута.')
    elif k[1] in casA: print('Время(веденное вами): '+k[0]+' часов '+k[1]+' минуты.')
elif k[0] in cas:
    if k[1] in casOV: print('Время(веденное вами): '+k[0]+' час '+k[1]+' минут.')
    elif k[1] in cas: print('Время(веденное вами): '+k[0]+' час '+k[1]+' минута.')
    elif k[1] in casA: print('Время(веденное вами): '+k[0]+' час '+k[1]+' минуты.')
elif k[0] in casA:
    if k[1] in casOV: print('Время(веденное вами): '+k[0]+' часа '+k[1]+' минут.')
    elif k[1] in cas: print('Время(веденное вами): '+k[0]+' часа '+k[1]+' минута.')
    elif k[1] in casA: print('Время(веденное вами): '+k[0]+' часа '+k[1]+' минуты.')

