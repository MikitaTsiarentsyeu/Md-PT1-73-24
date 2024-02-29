# 3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.


list_len_greater_5 = []

def len_greater_5(l:list):
    for i in l:
        if len(i) > 5:
            list_len_greater_5.append(i)
    return list_len_greater_5
    
l = ["Eve", "Alice", "Maybelline","Bob", "Kate", "Hanna", "Michael", "Christopher", "Andrew"]
print(len_greater_5(l))