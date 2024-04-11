def is_palindrome(s):

    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


test_string1 = input("Write Example: ")


print(f"'{test_string1}' is a palindrome: {is_palindrome(test_string1)}")

