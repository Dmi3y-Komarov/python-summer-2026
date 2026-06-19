print('#1')

squares = []

for x in range(1,10):
    squares.append(x * x)
print(squares,'\n')

print('#1.1')
squares = [x * x for x in range(1,10)]
print(squares)

print('#2')

nums = [int(x) for x in input('Write integer number: ').split()]

evens = [x for x in nums if x % 2 == 0]
print(evens)

print('#3')

words = [str(x) for x in input("Write some words: ").split()]

length = [len(word) for word in words]
wordDict = dict(zip(words, length))
print(wordDict)

print('#4')

chars = [ch for ch in set(str(input('Write something: ').split()))]
print(chars)

print('#5')

names = ['Oleg', 'Gleb', 'Bogdan', 'Praskovya']
points = ['10', '20', '30', '40']
namesDict = dict(zip(names, points))
print(namesDict)
