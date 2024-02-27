# Write a recursive function to reverse a string.

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

s = "Have a good day"
reversed_s = reverse_string(s)
print(reversed_s)
