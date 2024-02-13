s = input("Введи строки: ").split()
filtered_list = [word for word in s if len(word)>5]
print(filtered_list)