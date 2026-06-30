def count_vowels(text, lang='ru'):
    VOWELS = {
            'ru' : set('аеёиоуыэюяАЕЁИОУЫЭЮЯ'),
            'en' : set('aeiuyoAEIUYO')
            }

    vowels = VOWELS.get(lang, VOWELS['ru'])

    return sum(1 for ch in text if ch in vowels)

def rev(text):
    return text[::-1]

def is_palindrome(text):
    if text == rev(text):
        return True
    else:
        return False


