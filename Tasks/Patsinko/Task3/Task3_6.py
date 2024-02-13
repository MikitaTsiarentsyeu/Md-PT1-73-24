"6. Write a program that takes a string as input and returns the string with all vowels removed."

string = input('Enter the string: \n')
vowels = ['a', 'e', 'o', 'i', 'y', 'u']

for i in string:
    if i in vowels:
        string=string.replace(i, '')
print(string)
