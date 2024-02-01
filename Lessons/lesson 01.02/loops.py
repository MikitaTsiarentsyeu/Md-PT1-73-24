# while True:
#     print("how you doing?")

x = 0
while x < 10:
    print(x)
    x += 1 

l = list("test str")
i = 0
while i < len(l):
    print(l[i])
    i+=1

symbol = "test"

for symbol in l:
    print(symbol)

print(symbol)

i = 0
count = len(l)
while True:
    if i == count:
        break
    print(l[i])
    i+=1

l = [1]
for i in l:
    l.append(i)
    if len(l) == 10:
        break

print(l)

print(l)

i = -1
while i < 9:
    i+=1
    if i % 2 == 0:
        continue
    print(i)

for i in [1,0,1,0,1,0]:
    if i:
        continue
    print(i)

for i in l:
    continue
else:
    print("the else")


print("the end")