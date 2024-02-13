#8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
userDataString = (input("Enter number of elements(separator is space) : "))
numberList = userDataString.split(' ')

sumOfList = 0.0
for i in range(0, len(numberList)):
    numberList[i] = int(numberList[i])

for i in range(0, len(numberList)):
    sumOfList += float(numberList[i])

print(sumOfList)
averageOfList = sumOfList / float(len(numberList))
print(f"Average of your list is: {averageOfList}")