a = "global variable"
l = [1,2,3,4,5]
num = 5

def modify():
    # l = "test"
    l[0] += 0.1

modify()
print(l)

# def modify():
#     num += 0.1

# modify()
# print(num)


def test():
    a = "test variable"
    print(a)
    a = "new var"

test()
test()
test()

def another_test():
    print(a)

another_test()

# for a in a:
#     print(a)

print([a for a in a])

print("final value - ", a)