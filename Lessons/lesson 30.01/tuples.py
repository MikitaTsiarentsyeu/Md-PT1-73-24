t = (1,2,3,4,5)
print(t, type(t), len(t))

t = 1,2,3,4,5
print(t, type(t), len(t))

t = ()
print(t, type(t), len(t))

t = (1,)
print(t, type(t), len(t))

t = tuple("test str")
print(t)
print(t[0], t[-1], t[2:6], t[::-1])

print((1,2,3)+(4,5,6)*3)

# t[0] = 5
print([1,2,3] == (1,2,3))
t[0], t[-1] = t[-1], t[0]