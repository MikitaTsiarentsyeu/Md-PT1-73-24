
# x = 777
# print(id(x))
# y = x
# print(id(y))
# print(x, y)

# x = x+111
# print(id(x))
# print(id(y))
# print(x, y)

# x = [777]
# print(id(x))
# y = x
# print(id(y))
# print(x, y)
# x[0] += 111
# print(x, y)
# print(id(x), id(y))

l1 = l2 = [1,2,3]
print(l1 == l2)
print(id(l1) == id(l2))
print(l1 is l2)

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)

t1 = (1,2,3)
t2 = (1,2,3)
print(t1 is t2)

t1 = tuple([1,2,3])
t2 = tuple([1,2,3])
print(t1 is t2)

s1 = "test str"
s2 = "test str"
s3 = "test " + "str"
print(s1 is s2 is s3)

x = 1200
y = 1200
print(x is y)