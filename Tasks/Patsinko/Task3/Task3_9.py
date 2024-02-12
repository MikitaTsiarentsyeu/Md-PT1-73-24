'9. Write a program that takes a string as input and returns the string reversed.'
string = input('Enter the string: \n')
s =''
for i in range(len(string)-1,-1,-1):
    s += string[i]
print(s)

# string = string[::-1]
# print(string)