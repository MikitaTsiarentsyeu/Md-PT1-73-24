my_list = input("Введи список чисел: ").split()
sorted_list = sorted(my_list, reverse=True)
second_largest = sorted_list[1]
print(f"Второе по величине: {second_largest}")