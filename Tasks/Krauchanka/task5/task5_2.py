# 2. Write a function that takes a list of strings as an 
# argument and returns a new list of strings that are all reversed.

def reverse_str(str):
    list_str = []
    for s in str:
        list_str.append(s[::-1])
    return list_str

str = input("Enter words separated by spaces: ").split(" ")
string_reversed = reverse_str(str)
print(string_reversed)
