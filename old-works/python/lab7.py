#7

s = list(input('Введите ЛЮБОЙ текст и программа скажет, есть ли в нем цифры: '))
numbers = '1','0','2','3','4','5','6','7','8','9'

i = False

for char in s:
    if char in numbers:
        i = True
        break
print(i)

