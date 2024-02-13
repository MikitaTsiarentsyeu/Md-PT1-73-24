# 7. Write a program that takes a string as input and returns the 
# string with all capital letters converted to lowercase and vice versa.

str = input ("Write any line: ")
new_str = "" 
for i in str: 
    if i.isupper(): 
        new_str += i.lower() 
    else: new_str += i.upper() 

print(new_str)