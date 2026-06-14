#4 iz 1

k=int(input('Введите ваш возраст: '))
god='1'
godA='2','3','4'
let='5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'
if str(k%100) in let:print('Вам '+str(k)+' лет')
elif str(k%10) in let:print('Вам '+str(k)+' лет')
elif str(k%10) in god:print('Вам '+str(k)+' год')
elif str(k%10) in godA:print('Вам '+str(k)+' года')

