l = [chr(x*x) for x in range(100) if x%2==0 and x%5==0]
print(l)

l = []
for x in range(100):
    if x%2==0 and x%5==0:
            l.append(chr(x*x))
print(l)

# l = [print(x) for x in range(10)]
# print(l)

abc = ['a', 'b', 'c']
numbers = [1,2,3]

# for letter in abc:
#       for number in numbers:
#             print(f"{letter}-{number}")

l = [f"{letter}-{number}" for letter in abc for number in numbers]
print(l)

l = [[1,2,3], [4,5,6], [7,8,9]]
l = [y for x in l for y in x]
print(l)

l = {chr(x*x) for x in range(100) if x%2==0 and x%5==0}
print(l, type(l))

l = {x:chr(x*x) for x in range(100) if x%2==0 and x%5==0}
print(l, type(l))

l = (chr(x*x) for x in range(100) if x%2==0 and x%5==0)
print(l, type(l))

print([x for x in l])