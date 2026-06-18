print('#1')
nums = [1, 10, 4, 6, 7, 1, 0, 3, 9, 8, 4, 2]
result = set(nums)
print(result)

print('#2')
groupA = {'Oleg', 'Ignat', 'Gleb', 'Olga', 'Fedr'}
groupB = {'Petr', 'Fedr', 'Bartholomew', 'Helga'}
result = set(groupA | groupB)
print(groupA & groupB)
print(result)

print('#3')
text = 'hello world'
letters = set(text)
print(letters)

print('#4')

word1 = str(input('Write first word\n'))
word2 = str(input('Write second word\n'))

common = set(word1) & set(word2)
print(common)

print('#5')

math = ['Anton', 'Oleg', 'Gleb', 'Stepan']
phylosophy = ['Fedor', 'Sofia', 'Robert', 'Ivan', 'Oleg']

setPhylosophy = set(phylosophy)
setMath = set(math)
print(setMath & setPhylosophy)
print(setMath - setPhylosophy)

print('#6')

bag = ['bibki', 'beer', 'key', 'bibki']
sBag = set(bag)
sBag.add('knife')
sBag.remove('bibki')
print(sBag)
