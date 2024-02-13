'7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.'
string = input('Enter the string: \n')
s = ''
for i in string:
    conv=i.swapcase()
    s += conv
print(s)