num_list = list(map(int, input("Enter list of numbers: \n").split()))

prime_num = []
for i in num_list:
    if i > 1:
        for p in range(2, i // 2 + 1):
            if i % p == 0:
                break
            else:
                prime_num.append(i)

if len(prime_num):
    print(max(prime_num))
else:
    print("Prime number is not in list")
