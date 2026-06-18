print('#1')

country = dict(code='RU', name='Russia', population=143000000)

print(country.keys())
print(country.items())
print(country.values())

print('#2')
'''
text = 'hello world'
alphabet = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

probability = {}
counterOutside = 0
counterInside = 0
counter = 0
lenText = len(text)

for char in alphabet:
    counter = 0
    for sign in text:
        if char == sign:
            counter+=1
            counterInside+=1
    if counter>0:
        probability[char] = counter
print(probability)
'''
text = str(input('Write something\n'))
letters = set(text)
if (',' in text):
    letters.remove(',')
if ('.' in text):
    letters.remove('.')
if (' ' in text):
    letters.remove(' ')
result = {}

for char in letters:
    result[char] = text.count(char)
print(result)

print('#3')

firstDict = {'a':20, 'b':40, 'c':41}
secondDict = {'b':9, 'e':35, 'h':66}
result = {}

for key in firstDict:
    for sKey in secondDict:
        result[key]=firstDict.get(key, 0)+secondDict.get(key, 0)
        if key!=sKey:
            result[sKey]=firstDict.get(sKey, 0)+secondDict.get(sKey, 0)

print(result)


