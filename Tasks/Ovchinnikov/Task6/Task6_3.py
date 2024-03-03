# 3. Write a recursive function to count the number of occurrences of a given character in a string.

def CountSerchingCharacter(onCheckString, seekingChar):
    global globalCounter

    if len(onCheckString) == 0:
        return 0
    if(onCheckString[0] == seekingChar):
        globalCounter += 1
        
    CountSerchingCharacter(onCheckString[1:], seekingChar)

userData = input("Enter your string: ")
userOnSearchChar = input("Enter your character you're serching: ")

globalCounter = 0
CountSerchingCharacter(userData, userOnSearchChar)
print(f"Count:[{globalCounter}] of char:[{userOnSearchChar}] in string: {userData}")