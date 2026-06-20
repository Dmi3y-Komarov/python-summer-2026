print('#1')

names = ['Oleg', 'Gostomysl', 'Stepan', 'Alexander']
dictName = {number : name for number, name in enumerate(names, start=1)}
print(dictName)

print('#2')

text = str(input('Write something: '))
dictText  = {word : text.count(word) for word in text.split()}
print(dictText)
