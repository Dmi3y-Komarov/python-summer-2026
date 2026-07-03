def iinput(text):
    while True:
        try:
            number = int(input(text))
        except ValueError:
            print('Ошибка: Вы ввели не число!')
        else:
            return number

def upper_vowels(text, lang='ru'):
    lang = lang.lower()
    VOWELS = {
            'ru' : set('аеёиоуыэюяАЕЁИОУЫЭЮЯ'),
            'en' : set('aeiuyoAEIUYO')
            }

    if lang not in VOWELS.keys():
        return 'Ошибка: данный язык не поддерживается!'

    vowels = VOWELS[lang]

    return ''.join(char.upper() if char in vowels else char for char in text)
