# 7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.

input_string = input("Please enter text here\n")

new_string = ''
for i in input_string:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    new_string += i
print(new_string)