def outer():

    def inner():
        print("hello from inner")

    print("hello from outer")

    return inner
    
    
res = outer()
print(res, type(res))
res()


def operation(sign):
    if sign == "+":
        def oper(x, y):
            return x+y
    elif sign == "-":
        def oper(x, y):
            return x-y
    elif sign == "*":
        def oper(x, y):
            return x*y
    elif sign == "/":
        def oper(x, y):
            return x/y
        
    return oper

sum = operation("+")

def power_of(n):
    def power(x):
        return x**n
    return power

cube = power_of(3)
print(cube(2), cube(3))

square = power_of(2)
print(square(2), square(3))