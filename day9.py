print('#1')

text = input('Text: ')
print(f'Original text: {text}')
print(f'Lower text: {text.lower()}')
print(f'Upper text: {text.upper()}')

print('#2')

text = input('Text: ')
print(f'Words count: {len(text.split())}')

print('#3')

text = input('Text: ')
dictWords = {len(word) : word for word in text.split()}
print(f'Longest word: {dictWords[max(dictWords.keys())]}, length: {max(dictWords.keys())}')

print('#4')

text = input('Text: ')

dictWords = {word : text.count(word) for word in set(text.split())}
print(dictWords)

print('#5')

text = input('Text: ')
if text == text[::-1]:
    print(f'Palindrome')
else:
    print(f'Not palindrome')

print('#6')

text = input('Text: ')
dictWords = {word : text.count(word) for word in set(text.split())}

revText = text.split()[::-1]
for word in revText:
    if dictWords[word] > 1:
        indx = revText.index(word)
        for i in range(dictWords[word]):
            revText.pop(indx)
            indx = revText.index(word, indx + i + 1)
result = ' '.join(revText)
print(result)
