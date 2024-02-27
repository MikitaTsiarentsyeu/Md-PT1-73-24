# 1. Write a function that takes two integers as arguments and returns their sum.

def SumOfValues(FirstNumber, SecondNumber):
    return(FirstNumber + SecondNumber)

firstNumber = (int)(input("Enter first number:"))
secondNumber = (int)(input("Enter second number:"))
print(f"Sum of your numbers: {SumOfValues(firstNumber, secondNumber)}")