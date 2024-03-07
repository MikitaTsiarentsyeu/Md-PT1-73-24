input_string = input("Enter string: \n")

converted_string = ""

for i in input_string:
    if i.islower():
        converted_string += i.upper()
    else:
        converted_string += i.lower()

print(converted_string)
