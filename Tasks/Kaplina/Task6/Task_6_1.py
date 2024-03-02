# 1. Write a recursive function to reverse a string.

string = "Hello Kate!"

def reverse_str(string, i = 0, reversed = None):
    if not reversed:
        reversed = ''
    if i == len(string):
        return reversed
    reversed += string[-i-1]
    return reverse_str(string, i+1, reversed)

print(reverse_str(string))





