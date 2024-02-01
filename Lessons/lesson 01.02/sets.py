# l = [1,2,3,4]

# t = (1,2,3,4,5)

# d = {"one":1, "two":2}

s = {1, "two", 2.0}
print(s, type(s), len(s))

s = {1,1,1,1,1,1,1,1,1,1, "two", 2.0}
print(s, type(s), len(s))

s = {1, (1,2,3)}
print(s)

# s = {}
# print(s, type(s), len(s))

s = set()
print(s, type(s), len(s))

l = [1,1,1,1,2,2,3,4,5,56,6,7,8,8]
print(set(l))

string = "test str"
print(set(string))

print(hash(string))

l1 = [1,2,3,3,3,3]
l2 = [3,2,1]
print(l1 == l2)
print(set(l1) == set(l2))

s = set()
s.add(1)
s.add(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

s.update([4,5,6])
print(s)

s.update("test")
print(s)

s.add("test")
print(s)

s.remove(1)
print(s)

if 1 in s:
    s.remove(1)
    print(s)

s.discard(1)
print(s)

print(s.pop(), s)
print(s.pop(), s)
print(s.pop(), s)

s.clear()
print(s)

print({1,2,3,4,5}.intersection({3,4,5,6,7,8}))
print({1,2,3,4,5}.union({3,4,5,6,7,8}))