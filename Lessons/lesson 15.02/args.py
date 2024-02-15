l = [1,2,3,4,5]
x = "test"

def append(l, x):
    l.append(x)

def find(l, x):
    return l.index(x)

append([], 1)
print(l)


def sum(a,b,c):
    return a+b+c

sum(c=1,a=2,b=3)

def modify(value, modifier=-1, parameter=5):
    return (value*parameter)//modifier

print(modify(3))
print(modify(3, -2))
print(modify(3, -2, 10))

print(modify(3, parameter=-2))


def get_list(l=[]):
    l.append(1)
    print(l)

print(get_list())

l = [1,2,3,4,5]
print(get_list(l))

print(get_list())
print(get_list())
print(get_list())
print(get_list())