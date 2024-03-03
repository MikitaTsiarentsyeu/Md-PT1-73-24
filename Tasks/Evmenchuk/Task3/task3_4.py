number_list = [11, 2, 38, 4, 55, 46, 123, 1]

for i in range(len(number_list)-1):
    for j in range(len(number_list)-1):
        if number_list[j] > number_list[j+1]:
            number_list[j], number_list[j+1] = number_list[j+1], number_list[j]

print(number_list[-2])
