# 3. Write a recursive function to count the number of occurrences of a given character in a string.

string = 'Write a recursive function to count the number of occurrences of a given character in a string'
char = 'a'

def count_char(string, char, i = 0):

    if i == len(string):
        return False

    count = 0
    if string[i] == char:
        count = 1

    if len(string) == 1:
        return char
    else:
        return count + count_char(string, char, i+1)

print(count_char(string, char))

