#4. Write a program that takes a list of numbers as input and returns the second largest number in the list.
userDataString = (input("Enter number of elements(separator is space) : "))
numberList = userDataString.split(' ')

for i in range(0, len(numberList)):
    numberList[i] = int(numberList[i])

for j in range(0, len(numberList) - 1):
    for i in range(0, len(numberList) - 1):
        if numberList[i] > numberList[i+1]:
            tempValue = numberList[i]
            numberList[i] = numberList[i+1]
            numberList[i+1] = tempValue

print(f'Second largest number is: {numberList[-2]}, largest number is: {numberList[-1]}')