'''4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, second for count of the upper case letters in the initial string.
'''


def func(string:str):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper +=1
        elif i.islower():
            lower += 1
        else:
            continue
        
    return upper, lower

