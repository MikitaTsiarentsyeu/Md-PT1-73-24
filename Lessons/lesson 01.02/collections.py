l = [[1,2,3], [4,5,6], [7,8,9]]

print(l)
print(l[0][0])
print(l[1][1])
print(l[2][2])

# l = []
# l.append(l)
# print(l)
# print(l[0][0][0][0][0][0])


t = (l, "test")
print(t)
t[0][0][0] = 1.0
print(t)

d = {(1,2,3):"value"}
print(d, d[(1,2,3)])
# d[t] = "tuple" error
# print(d)