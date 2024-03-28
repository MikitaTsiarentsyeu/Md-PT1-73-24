# 1. Write a recursive function to reverse a string.

def ReverseStringRecur(nonReversedString):
    global reversedString
    if(len(nonReversedString) <= 0):
        return reversedString

    reversedString += nonReversedString[-1]
    nonReversedString = nonReversedString[:-1]

    return ReverseStringRecur(nonReversedString)
        
reversedString = ""
userData = input("Enter your string: ")
reversedString = ReverseStringRecur(userData)
print(f"Reversed string {userData} -> {reversedString}")