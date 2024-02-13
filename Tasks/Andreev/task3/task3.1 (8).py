s = input("Список чисел: ").split()
for i in range(len(s)):
    s[i] = int(s[i])
#average = sum(numbers) / len(numbers)
total = sum(s)
average=sum(s)/len(s)
print("Среднее:", average)