"""6. Write a program that takes a string as input and returns the string with all vowels removed."""

string = input('Enter string:\n').casefold()

vowels = list('aeiouy')

for i in string:
    if i in vowels:
        string = string.replace(i, '')
        

print(f'Your string without vowels: {string}')
