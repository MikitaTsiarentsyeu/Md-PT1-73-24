test_func = 5
print(test_func, type(test_func))
test_func = "test"
print(test_func, type(test_func))

def test_func():
    print("the function is working!")
print(test_func, type(test_func))

test_func()

def first():
    print("this is first")
    second()

def second():
    print("this is second")

first()


def sum_of_three(a, b, c):
    res = a+b+c
    return res

print(sum_of_three(3,2,1))

def modify_int(value):
    print(id(value))
    value += 2
    print(id(value))
    print(value)
    return value

x_value = 5
print(id(x_value))
x_value = modify_int(x_value)
print(id(x_value))
print(x_value)



def modify_list(value):
    print(id(value))
    value.append(2)
    print(id(value))
    print(value)

x_value = [5]
print(id(x_value))
modify_list(x_value)
print(id(x_value))
print(x_value)


def choose_day(day):
    return "test", [1,2,3,4,5], 2.0

    if day == "monday":
        return "time to go to work"
    if day == "saturday":
        return "time to rest"
    
    return "wait for it"
    
res1, res2, res3 = choose_day("tuesday")
# print(res, type(res))
print(res1, res2, res3)