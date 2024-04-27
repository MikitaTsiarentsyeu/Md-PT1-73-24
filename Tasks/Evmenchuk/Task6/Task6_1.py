s = input('Enter your string: \n')


def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]


print(rreverse(s))
