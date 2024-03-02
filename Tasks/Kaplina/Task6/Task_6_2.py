# 2. Write a recursive function to check whether a given string is a palindrome.

string = "А роза упала на лапу Азора"

formatted_str = string.replace(' ', '').lower()
print(formatted_str)


def check_palindrome(formatted_str, i = 0):

    if i >= len(formatted_str) // 2:
        return True
    if formatted_str[i] == formatted_str[-i-1]:
        return check_palindrome(formatted_str, i + 1)
    else:
        return False


if check_palindrome(formatted_str):
    print("This string is a palindrome")
else:
    print("Not a palindrome")
