num_list = list(map(float, input("Enter list of numbers: \n").split()))

sum_num_list = 0

for i in range(len(num_list)):
    sum_num_list += num_list[i]

avrg = sum_num_list/len(num_list)

print(avrg)
