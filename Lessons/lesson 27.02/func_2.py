

def cycle(l, f):
    for i in l:
        f(i)

def sq(x):
    print(x*x)

# (lambda x: print(x*x))(12)
sq = lambda x: print(x*x)
sq(12)

# def sq(x):
#     return x*x

# sq = lambda x: x*x

l = [1,2,3,4,5]
cycle(l, print)
cycle(l, sq)
cycle(l, lambda x: print(chr(x*100)))

(lambda x, y=0: print(x*y))(2)

test_str = "Abc Aac aaa test"
print(sorted(test_str.split()))

print(ord('A'), ord('a'))

print(sorted([x.lower() for x in test_str.split()]))

print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

def lwr(x):
    return x.lower()

print(sorted(test_str.split(), key=lwr))

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l))
# print(sorted([[4,5,6], [7,8,9], [1,2,3]]))
print(sorted(l, key=lambda x: x[1]))

