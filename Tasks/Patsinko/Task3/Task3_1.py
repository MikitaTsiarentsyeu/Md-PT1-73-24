"1. Write a program that takes a string as input from a user and returns the number of vowels in the string."
string = input('Enter the string: \n')
vowels = ['a', 'e', 'o', 'i', 'y', 'u']

number_v = 0
for i in string:
    if i in vowels:
        number_v += 1
print(number_v)