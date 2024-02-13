#2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.
userDataString = (input("Enter number of elements(separator is space) : "))
numberList = userDataString.split(' ')

for i in range(0, len(numberList)-1):
    numberList[i] = int(numberList[i])

sumOfEvenNumbers = 0

for i in range(0, len(numberList)-1):
    if(numberList[i] % 2 == 0):
        sumOfEvenNumbers += numberList[i]

print(f"Sum of even numbers is: {sumOfEvenNumbers}")