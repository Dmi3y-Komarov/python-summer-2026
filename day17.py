print('#1')

while True:
    try:
        numbet = int(input('Введиье число: '))
    except ValueError:
        print('Ошибка: введите число')
    else:
        break

print('#2')

import os

file_path = input('Введите путь к файлу: ')

file_path = os.path.normpath(file_path)
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('Ошибка: файл не обнаружен!')

print('#3')

def input_int(text):
    text = str(text)
    while True:
        try:
            number = int(input(text))
        except ValueError:
            print('Ошибка: введите число!')
        else:
            return number
            break

a = input_int('Введите число a: ')

b = input_int('Введите число b: ')

try:
    c = a/b
except ZeroDivisionError:
    print('Ошибка: на ноль делить нельзя!')
else:
    print(f'{a}/{b} = {c}')
