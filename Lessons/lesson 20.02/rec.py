def level1():
    print("start of level1")
    level2()
    print("end of level1")

def level2():
    print("\tstart of level2")
    level3()
    print("\tend of level2")

def level3():
    print("\t\tstart of level3")
    level4()
    print("\t\tend of level3")

def level4():
    print("\t\t\tstart of level4")
    level1()
    print("\t\t\tend of level4")

# level1()
    
def recursion(counter=0):
    if counter == 4:
        return
    print("I'm recursive")
    recursion(counter+1)

recursion()

def print_n_times(text, n=10):
    if n == 0:
        return
    print(text)
    print_n_times(text, n-1)


# 1! = 1
# 2! = 2*1!
# 3! = 3*2!
# 4! = 4*3!
# 5! = 5*4!

# n! = n*(n-1)!
    
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))


num = 120

def digit_sum_str(num, i=0, res=0):
    num = str(num) if isinstance(num, int) else num
    if i == len(num):
        return res
    res += int(num[i])
    return digit_sum_str(num, i+1, res)

print(digit_sum_str(num))

def digit_sum(num):
    if num == 0:
        return 0
    return digit_sum(num//10) + (num % 10)

print(digit_sum(num))


l = [1,[[[2]]],[3], [4,5,6, [7,8,9, [10, 11, 12]]]]

def flatten(l, res=None):
    if not res:
        res = []
    for i in l:
        if isinstance(i, int):
            res.append(i)
        else:
            flatten(i, res)
    return res

print(flatten(l))