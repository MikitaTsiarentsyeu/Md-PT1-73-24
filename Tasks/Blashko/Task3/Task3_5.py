"""5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.
"""

list_string = input('Enter list of strings:\n').split()
result = [i for i in list_string if len(i)>5]
print(result)

