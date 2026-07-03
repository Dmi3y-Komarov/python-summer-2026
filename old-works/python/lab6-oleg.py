#6Oleg

while True:
    s = input('Введите 24 числа: ').split()

    if len(s)!=24:
        print('Ошибка: Вы ввели не 24 числа')
    else:
        break

s.reverse()
print(f'{s[:6]}\n{s[6:12]}\n{s[12:18]}\n{s[18:]}')
