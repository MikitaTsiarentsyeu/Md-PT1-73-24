'''2. Write a recursive function to check whether a given string is a palindrome.'''


def is_palindrom(string:str):
    string = string.casefold().replace(' ', '')
    start, finish = 0, len(string)-1
    if len(string) <= 1:
        return True
    if string[start] != string[finish]:
        return False
    return is_palindrom(string[start+1:finish])
    
                 
s = input('Enter a string to check whether a given string is a palindrome:\n')  

print(is_palindrom(s))
