"""1. Write a program that takes a string as input from a user and returns the number of vowels in the string."""

string = input('Enter string:\n').casefold()
vowels = list('aeiouy')
count_vowels = 0

for i in string:
    if i in vowels:
        count_vowels += 1
        
print(f"Your string '{string}' includes {count_vowels} vowels")
        
