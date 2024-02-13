# 6. Write a program that takes a string as input 
# and returns the string with all vowels removed.

str = input ("Write any line: ")
vowels = list("aeiouy")
res=""
for i in str:
    if i.lower () not in vowels:
        res+= (i)

print(res)


# OTHERWISE


str_str = input("Write any line: ")
vowels = list("aeiouy")
for i in str_str:
    if i.lower () in vowels:
        str_str = str_str.replace(i, '')
        
print(str_str)


