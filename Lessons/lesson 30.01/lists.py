l = [1,2,3,4,5]
print(type(l), l, len(l))

l = []
print(type(l), l, len(l))

s = "test"
l = ['t', 'e', 's', 't']
print(s, l)

l = [1, "two", 3.0, [4]]
print(l)

print([1,2,3]+[4,5,6])
print([1]*3)

l = list("test string")
print(l)

print(l[0], l[1], l[2])
print(l[-1], l[-2], l[-3])
print(l[:5])
print(l[::-1])

# print(l[100]) error

l[0] = "f"
print(l)

l[0] = 4
print(l)
print(l[0])

x = "t"
l[0] = x
print(l)

l[0] = 4
print(x)

l.append("end")
print(l)

l.extend("end")
print(l)

l.insert(0, "start")
print(l)

l.remove('s')
print(l)

if 's' in l:
    l.remove('s')
    print(l)

print(l.pop())
print(l.pop())
print(l.pop())
print(l)

print(l.pop(0))
print(l.pop(0))
print(l.pop(0))
print(l)

x = 5
l[0] = x
print(l)
del l[0]
print(l)
print(x)
del x
# print(x) error

del l[1:5]
print(l)

l.clear()
print(l)

s1 = "two"
s2 = "one"
print(s1 == s2)

l1 = list(s1)
l2 = list(s2)
print(l1 == l2)

print(s1 == l1)

l = [1,2,3,4,5]
# swap = l[-1]
# l[-1] = l[0]
# l[0] = swap
# print(l)
l[0], l[-1] = l[-1], l[0]
print(l)