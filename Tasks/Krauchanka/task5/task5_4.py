# 4. Write a function that takes a string as an argument and returns two numbers, 
# first for count of lower case letters, second for count of the upper case letters in the initial string.

def letter_selection (string):
    lowercase_letter=0
    uppercase_letter=0
    for letter in string:
        if letter.islower ():
            lowercase_letter+=1
        elif letter.isupper():
            uppercase_letter+=1
    return lowercase_letter, uppercase_letter
    
string = input("Enter your text: ")
lowercase_letter, uppercase_letter = letter_selection(string)

print(lowercase_letter, uppercase_letter)

