# 3. Write a function that takes a list of strings as an argument 
# and returns a new list with all the strings that have a length greater than 5.

def string_length (string):
    return [s for s in string if len(s)>5]

string = input("Enter your world separated by spaces: ").split(" ")
sorted_string = string_length(string)
print(sorted_string)