
anotherOne = True
while(anotherOne):
    anotherOne = False

    print("#1")
    
    words = ["cat", "car", "crown", "coconut"]
    
    for number, word in enumerate(words):
        
        print(f"Word #{number+1}: {word}")

    print("#2")
    
    flag = True
    marker = True
    while(marker):
        wantedWord = str(input("Write word, what position you want to know?\n"))
        words = ["bibki", "cake", "glass", "grass", "green", "green", "beer", "tusk", "task"]
        
        if (wantedWord == "I want to see words") or (wantedWord == "I want to see array"):
            print(words)
        else:
            for number, word in enumerate(words):
                if word == wantedWord:
                    print(f"Word {wantedWord} first time i see on position {number} (start count from 0)")
                    marker = False
                    flag = False
                    break
            if flag:
                print(f"Word {wantedWord} not in array")

    print("#3")
    
    nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 99]
    print(nums)
    
    for number, value in enumerate(nums):
        if number%2 and value%2:
            nums[number] = 0
    print(nums)
    
    print("#4")
    
    peoples = ["Oleg", "Akakiy", "Seraphim", "Glubokoslav"]
    points = [88, 67, 14, 96]
    students = {}
    for i, value in enumerate(zip(peoples, points)):
        students[i] = value
    print(students)
    
    print("#5")
    
    elements = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    marker = True
    while(marker):
        number = int(input("Write number of element what you want to use like zero point(beetwen 0 and 25)\n"))
        if number>=0 and number<26:
            marker = False
            for position, value in enumerate(elements[number:], start = number):
                print(f"Index {position}: {value}")
        else:
            print("You number out of range (0, 25), tru again")
    
    print("end of programm")
    answer = str(input("You want start programm one more time¿?(Y/n)"))
    yAnswer = ["y", "Y", "yes", "Yes", "Hell fucking yeah man!"]
    nAnswer = ["n", "N", "no", "No", "Nope", "nope", "no thanks", "No thanks", "go fuck youreself, bro"]
    if answer in yAnswer:
        anotherOne = True
