#8
while True:

    m0 = input('Введите 20 чисел в любом порядке, в качестве разделителя используйте пробел: ').split()
    if len(m0)!=20:
        print('Ошибка: по условию надо 20 чисел!')
    try:
        m = [int(x) for x in m0]
    
    except ValueError:
        print('Ошибка: вы введи не числа!')
    
    else:
        break

#print(m)
m.sort()
#print(m)

result = [number for number in m if number%2 != 0]
print(result)
