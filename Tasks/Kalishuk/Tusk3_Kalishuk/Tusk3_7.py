input_string = input("Please enter text here\n")

new_string = ''
for i in input_string:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    new_string += i
print(new_string)