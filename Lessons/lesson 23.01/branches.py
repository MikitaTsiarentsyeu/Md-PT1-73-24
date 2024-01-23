x = 20

if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
else:
    print("idk")


if x >= 0:
    if x > 0:
        print("it's positive")
    else:
        print("it's zero")
else:
    print("it's negative")


print("that's all")


x = 5

if x == 5:
    print("it's five")
else:
    print("it's not")

print("it's five") if x == 5 else print("it's not")

x = 1
if x % 2 == 0:
    res = "even"
else:
    res = "odd"
print(res)

res = "even" if x % 2 == 0 else "odd"
print(res)