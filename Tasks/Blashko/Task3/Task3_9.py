"""9. Write a program that takes a string as input and returns the string reversed.
"""

string = input('Enter string:\n')

new_string = ''.join([string[-x] for x in range(1, len(string)+1)])

print(f'Reversed string:  {new_string}')

