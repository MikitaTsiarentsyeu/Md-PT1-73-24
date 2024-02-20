my_list=input("Ведите список чисел: ").split()
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
total = sum(my_list)
total = 0
for num in my_list:
    if num% 2==0:
        total += num
print("Сумма четных чисел:", total)