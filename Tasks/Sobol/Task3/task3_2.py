numbers = list(map(int, input("Input values: ").split()))
sum = 0
for i in numbers:
    if (i % 2 == 0):
        sum += i
print(sum)        