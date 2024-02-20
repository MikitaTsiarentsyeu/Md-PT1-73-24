
def sum(x, y):
    return x+y

sum(2, 3)
sum(y=2, x=3)

def divide(x, y, is_round=True, round_pos=1):
    res = x/y
    if is_round:
        res = round(res, round_pos)
    return res

print(divide(1, 3))
print(divide(1, 3, False))
print(divide(1, 3, round_pos=3))


# print(1,2,3,4,5,6,7,8,9,10)

def sum(*args):
    res = 0
    for arg in args:
        res += arg
    return res

print(sum(1,2,3,4,5,6))
# print(sum(1,2,3,4,5,6,7,8,9,10,"test")) error

def sum(*args, a=1, b=2):
    print(a, b)
    res = 0
    for arg in args:
        res += arg
    return res

print(sum(3,4,5,6,a=10,b=20))

print(sum(*[3,4,5,6],a=10,b=20))

print(*[1,2,3,4,5])



def print_variables(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

print_variables(a=1, b=2, c=3, test="test", abc45=45)


def my_print(*args, sep=' ', **kwargs):
    if 'end' in kwargs:
        print(*args, sep=sep, end=kwargs['end'])
    else:
        print(*args, sep=sep)

my_print(1,2,3,4,5, sep=',')
my_print(1,2,3,4,5, sep=',', end='.\n')