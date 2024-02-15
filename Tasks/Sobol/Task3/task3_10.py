lst = list(map(int, input("Input values: ").split()))
new_lst = []
for i in range(0, len(lst)):
    flag = 0
    for j in range(2, int((lst[i])) // 2):
        if (lst[i] % j) == 0:
            flag += 1   
    if (flag == 0):        
        new_lst.append(int(lst[i]))    
max_prime_number = max(new_lst)
print("Maximum prime number is:", max_prime_number)        