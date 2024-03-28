'''1. Write a recursive function to reverse a string.'''


def reverse_string(string:str):
    if len(string) == 1:
        return string[-1]
    return string[-1] + reverse_string(string[:len(string)-1])
    
    
s = input('Enter a string to reversing it:\n')    
print(reverse_string(s))
