# 9. Write a program that takes a string as input and returns the string reversed.


input_string = input("Please enter text here\n")

# Case 1
print(input_string[::-1])

# Case 2
new_string = ''
for i in range(len(input_string)):
    new_string += input_string[len(input_string) - i - 1]
print(new_string)





