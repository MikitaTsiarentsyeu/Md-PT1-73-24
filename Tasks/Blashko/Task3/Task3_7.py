"""7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.
"""

string = input('Enter string:\n')

converted_string = ''

for i in string:
    if i.islower():
        converted_string += i.upper()
    else:
        converted_string += i.lower()
        
print(converted_string)
