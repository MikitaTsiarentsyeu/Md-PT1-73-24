import time

# def do_twice(func, param1, param2):
#     func(param1, param2)
#     func(param1, param2)

def do_twice(func):
    def wrapper(param1, param2):
        func(param1, param2)
        func(param1, param2)
    return wrapper

users = {"user1":hash("test")}

def auth(func):
    def wrapper(*args):
        name = input("enter your user name:")
        if name in users:
            password = input("enter your password:")
            if hash(password) == users[name]:
                return func(*args)

        print("wrong user name or password")   

    return wrapper 

@auth     
@do_twice
def test_func(x, y):
    print(f"hello, I'm test func, my parameters - x:{x} and y:{y}")

# test_func_do_twice = do_twice(test_func, 1, 2)
# test_func_do_twice()

# test_func = do_twice(test_func, 1, 2)
# test_func()
# test_func = auth(test_func, 1, 2)
test_func(1,2)


def time_it(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        finish = time.time()
        time_res = finish-start
        print(time_res)
        return res, time_res

    return wrapper

@time_it
def test_cycle(x):
    count = 0
    for i in range(10000):
        if i%x==0:
            count += 1
    return count

print(test_cycle(9))