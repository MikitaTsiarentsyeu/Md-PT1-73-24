# num = 5

def modify():
    global num
    num = 5
    num += 1
    print(num)

modify()
# print(num)

x = "global"

def outer():
    x = "outer"
    num = 3 

    def inner():
        x = "inner"
        nonlocal num
        num += 2
        print(x)

    print(x)
    inner()
    print(x)

outer()


