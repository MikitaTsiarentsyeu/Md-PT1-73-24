str_list = input("Enter list of string: \n").split()

returns = [i for i in str_list if len(i) > 5]

print(returns)
