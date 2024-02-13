# 1. Write a program that takes a string as input from a 
# user and returns the number of vowels in the string.

str = input ("Write any line: ")
vowels = list("aeiouy")
count = 0
for i in str:
    if i.lower () in vowels:
        count += 1
        print (i)
print ( "vowels namber in the string -", count)