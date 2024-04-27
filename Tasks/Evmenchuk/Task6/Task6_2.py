a = input("Enter your string:\n")


def pal(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return pal(s[1:-1])
        else:
            return False


if (pal(a) == True):
    print("This string is a palindrome!")
else:
    print("This string is not a palindrome!")
