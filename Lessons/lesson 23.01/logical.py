print(True, False)
print(type(True), type(False))

print(isinstance(1, int), isinstance(True, int), isinstance(False, int))

print(10*False + 3*True)

print(bool(-10), bool(10.1), bool(0.00000000000000000000000000000001))
print(bool("test"), bool(print), bool(bool))

print(bool(0), bool(""), bool([]), bool(None))

print(bool(print), bool(print()))

x = print()
print(x, type(x))

x = 5
print(x > 0)
print(True == False)
print(False == 0)

print(x > 0 and x < 100)
print(0 < x < 100) # 0 < x and x < 100

print(True or False)

print("left") and print("right")
not print("left") or print("right")