string = input("Input string:")
result = ""
input_string = string
for i in range(len(string)):
    result = input_string[i] + result
print("Result: ", result)    