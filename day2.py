#1

print("#1")
graders = []

for i in range(3):
    graders.append(5-i)
print(graders)

#2

print("#2")
teamA = ["Anton", "Joe"]
teamB = ["Susanna", "Fedor"]

teamA.extend(teamB)
print(teamA)

#3

print("#3")
chars = []
word = "hello"

for i in range(len(word)):
	chars.append(word[i])
print(chars)

#4

print("#4")
data = [10, 20, 68]

data1 = []
data2 = []
data1.extend(data)
data2.extend(data)

data1.append(data)
data2.extend(data)

print(data1)
print(data2)

#5

print("#5")
fruits = ["aple", "orange"]

print(fruits)

fruits.append("banana")
print(fruits)
fruits.extend(["kivi","mango"])
print(fruits)
fruits.append("dragon fruit")
print(fruits)

#6

print("#6")
nums = [1, -50, 39, 50, 2, -6, 7, 9, -34, -3, -9, 0]
positive = []
negative = []
for i in nums:
	if i >= 0: positive.append(i)
	else: negative.append(i)
print(positive)
print(negative)


