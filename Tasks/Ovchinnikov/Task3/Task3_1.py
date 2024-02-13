#1. Write a program that takes a string as input from a user and returns the number of vowels in the string.
vowelsConst = ['a', 'e', 'i', 'o', 'u', 'y']

userData = input("Input you sentece:")
vowelsCount = 0

for vowelLetter in vowelsConst:
    vowelsCount += userData.count(vowelLetter)

print(f"Number of vowels in string: {vowelsCount}")