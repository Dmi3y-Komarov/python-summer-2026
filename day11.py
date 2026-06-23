import os

def countLines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return len(file.readlines())
def makeFile(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        return 1

cantBeFirst = ['/', '*', '?', ' ', ':', ';', '|', '<', '>']
while(True):
    FILE_NAME = str(input("Write file name: "))
    if FILE_NAME[0] in cantBeFirst:
        print('This symbol cant be first!')
    else:
        if '.' not in FILE_NAME:
            FILE_NAME+='.txt'
            print(f'File name update: {FILE_NAME}')
        break
if not os.path.exists(FILE_NAME):
    x = makeFile(FILE_NAME)

print(countLines(FILE_NAME))

