#3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

def ChooseStringsBiggerThenLimitation(stringList):
    longStringList = []
    for i in range(len(stringList)):
        if(len(stringList[i]) > 5):
            longStringList.append(stringList[i]) 
            
    return longStringList

stringList = input("Write your strings by space separator: ").split()
print(ChooseStringsBiggerThenLimitation(stringList))