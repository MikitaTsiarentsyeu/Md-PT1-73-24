lst = list(map(int, input("Input values: ").split()))
sum_of_lst = 0
for i in range(len(lst)):
    sum_of_lst += lst[i]
average = sum_of_lst/len(lst)
print("Average = ", average)    
