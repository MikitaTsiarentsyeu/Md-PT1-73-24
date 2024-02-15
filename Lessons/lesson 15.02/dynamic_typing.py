l = []

def append(l:list):
    l.append(1)

# append(5)
    
def times(a, b):
    return a*b

print(times(2, 3))
print(times(2.5, 3))
print(times([2], 3))
print(times('2', 3))


def times_for_int(a:int, b:int) -> int:
    """this function will multiply only int values
    parameters:
    a - first int value
    b - second int value
    result:
    int product of a and b"""

    if isinstance(a, int) and isinstance(b, int):
        return a*b
    


def eq(coll1, coll2):
    for i in coll1:
        if i not in coll2:
            return False
    for i in coll2:
        if i not in coll1:
            return False 

    return True

def eq(coll1, coll2):
    return set(coll1) == set(coll2)

print(eq([1,2,3,3,3,3,3,3,3,3], [3,2,1]))
print(eq((1,2,3), (1,2,3)))
print(eq([1,2,3], (1,2,3)))
print(eq(['1','2','3'], "123"))



# def sum(a, b):
#     return a+b

# def sum(a, b, c):
#     return sum(sum(a, b), c)

# sum(1,2,3)

def my_print(arg):
    pass

print = my_print
print("test")