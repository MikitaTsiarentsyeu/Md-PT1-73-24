# s = "test str"
# l = list(s)
# print(l)

# f = 10.5
# i = int(f)
# print(i)

s = "test str"
s = {1:"one", 2:"two"}
# l = list(s)
l = []
for i in s:
    l.append(i)
print(l)

l = [1,2,3,4,5]
i = iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) error