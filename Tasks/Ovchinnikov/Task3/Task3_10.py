#10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.
primeNumbersConst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 
                     89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 
                     181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 
                     281, 283, 293]

userDataString = (input("Enter number of elements(separator is space) : "))
numberList = userDataString.split(' ')
primeNumberList = []

for i in range(0, len(numberList)):
    numberList[i] = int(numberList[i])

for i in range(0, len(numberList)):
    if(numberList[i] in primeNumbersConst):
        primeNumberList.append(numberList[i])

for j in range(0, len(primeNumberList)-1):
    for i in range(0, len(primeNumberList)-1):
        if primeNumberList[i] > primeNumberList[i+1]:
            tempValue = primeNumberList[i]
            primeNumberList[i] = primeNumberList[i+1]
            primeNumberList[i+1] = tempValue

print(f"Your highest prime number is: {primeNumberList[-1]}, prime number list:{primeNumberList}")