# 9. Write a program that takes a string 
# as input and returns the string reversed.

str = input ("Write any line: ")
new_str="" 
for i in range(len(str)-1,-1,-1):
    new_str+= str[i]

print(new_str)


# OTHERWISE


str = input ("Write any line: ")
new_str=str[::-1]
print(new_str)
