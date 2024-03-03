# 4. Write a recursive function to calculate the power of a given number.

def PowerOfNumber(number, degree):
    if degree == 1:
        return number
    else:
        return number * PowerOfNumber(number, degree - 1)

userNumber = input("Enter your number: ")
userDegree = input("Enter your degree: ")

print(f"Number in power[{userNumber}^{userDegree}], is:[{PowerOfNumber((int)(userNumber), (int)(userDegree))}]")