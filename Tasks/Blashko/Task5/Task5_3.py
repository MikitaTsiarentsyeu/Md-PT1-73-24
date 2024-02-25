'''3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.
'''


def func(list_strings:list): 
    return [i for i in list_strings if len(i)>5]
    
    
