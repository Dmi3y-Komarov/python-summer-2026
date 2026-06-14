#6Oleg

s=input('Введите 24 числа: ').split()

if len(s)!=24:print('Error');quit()
s.reverse()
print(f'{s[:6]}\n{s[6:12]}\n{s[12:18]}\n{s[18:]}')
