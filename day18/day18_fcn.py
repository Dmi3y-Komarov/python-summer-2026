def hello():
    name = str(input('Введите ваше имя: '))
    print(f'Привет, {name}')
    return

#=======================
def get_int(text):
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print('Ошибка: вы ввели не число!')
        else:
            return num

def power(num=None, p=None):
    if num==None:
        num = get_int('Введите число для возведения в степень: ')
    if p==None:
        p = get_int('Введите степень, в которуб зотите возвести число: ')
    if p == 0:
        return 1
    elif p == 1:
        return num
    elif p>1:
        return num * power(num, p-1)
#============================

