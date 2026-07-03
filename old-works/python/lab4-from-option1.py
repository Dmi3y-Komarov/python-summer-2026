from utils import iinput
#4 iz 1

k = iinput('Введите ваш возраст: ')

god = '1'
godA = '2','3','4'
let = '5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'
if (str(k%100) in let) or (str(k%10) in let):
    print(f'Вам {k} лет')
elif str(k%10) in god:
    print(f'Вам {k} год')
else:
    print(f'Вам {k} года')
