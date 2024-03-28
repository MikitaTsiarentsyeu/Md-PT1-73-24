# 2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.


def string_reverted(l:list):
    return l[::-1]

l = ["Eve", "Alice", "Maybelline","Bob", "Kate", "Hanna", "Michael", "Christopher", "Andrew"]
print(string_reverted(l))