#4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, second for count of the upper case letters in the initial string.

def CountUpperAndLowerCases(checkString):
    lowerCount = upperCount = 0

    for char in checkString:
        if char.islower():
            lowerCount += 1
        elif char.isupper():
            upperCount += 1

    return lowerCount, upperCount

userString = input("Enter your text: ")
lowerCount, upperCount = CountUpperAndLowerCases(userString)
print(f"Lowercase count: {lowerCount}, Uppercase count:{upperCount}")