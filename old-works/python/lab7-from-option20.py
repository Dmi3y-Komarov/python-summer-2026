#7 iz 20

from utils import upper_vowels

lan = str(input('Введите язык, на котором хотите написать текст, в формате: ru или en: '))
s = input('Введите любой текст на одном языке: ')

s = upper_vowels(s, lan)

print(s)

