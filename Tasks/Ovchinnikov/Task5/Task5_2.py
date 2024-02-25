# 2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.

def ReverseAllStrings(stringList):
    for i in range(len(stringList)):
        stringList[i] = (stringList[i])[::-1]
    return stringList

stringList = input("Write your strings by space separator: ").split()
print(ReverseAllStrings(stringList))