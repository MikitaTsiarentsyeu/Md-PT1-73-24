my_list = [1,99,200,14,18]
new_list = set(my_list)

new_list.remove(max(new_list))
print(new_list)
print(max(new_list))