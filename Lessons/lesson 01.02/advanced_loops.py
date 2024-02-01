for i in range(10):
    print(i)

for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)

test = "test str"
for i in range(len(test)):
    print(i, test[i])

print(list(range(1, 11, 2)))

for i in range(5):
    print("how you doing?")

for pair in enumerate(test):
    print(pair)

for i, e in enumerate(test):
    print(i, e)