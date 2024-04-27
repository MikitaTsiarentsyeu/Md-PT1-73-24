string = input('Enter your string: \n')
ch = input('Enter the character to check: \n')


def check(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:], ch)
    else:
        return check(string[1:], ch)


print('Number of occurrences:')
print(check(string, ch))
