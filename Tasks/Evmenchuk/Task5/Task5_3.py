str = ['I', 'live', 'in', 'Belarus', 'with', 'my', 'family']
str_2 = []


def func(str):
    for i in str:
        if len(i) > 5:
            str_2.append(i)
    return (str_2)


print(func(str))
