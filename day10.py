print('#1')

def powd(numb,powdr):
    return 1 if numb == 1 or powdr == 0 else (numb * powd(numb, powdr - 1) if powdr > 1 else numb)

number = int(input('Write number what you want: '))
powder = int(input('Write powder what you want: '))
print(powd(number,powder))

print('#2')

def max3(a, b, c):
    return a if a > b and a > c else (b if b > c else c)
numb1 = int(input('Write n1: '))
numb2 = int(input('Write n2: '))
numb3 = int(input('Write n3: '))
print(max3(numb1, numb2, numb3))

print('#3')

def isPalindrome(word):
    return True if word == word[::-1] else False

print(isPalindrome(str(input('Write something: '))))

print('#4')

def countWord(text):
    c = 0
    for word in text.split(): c+=1
    return c
text = str(input('Write something: '))
print(countWord(text))

print('#5')

def wordFrequency(text):
    sText = text.split()
    return {word : sText.count(word) for word in set(sText)}
text = str(input('Write something: '))
print(wordFrequency(text))
