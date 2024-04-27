def func(str):
    up = 0
    low = 0
    for i in str:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        else:
            pass
    return (up, low)


print(func(str('I live in Belarus')))
