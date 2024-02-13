# 5. Write a program that takes a list of strings as input and returns a list with all 
# strings that have a length greater than 5 characters.


str = input ("Write any line: ").split()
res = [a for a in str if len(a)>5]
print (res)