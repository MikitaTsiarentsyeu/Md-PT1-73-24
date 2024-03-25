str = input("Enter a string:\n")

converted_str = ''

for i in range(0,len(str)):
    if str[i].islower() == True:
        converted_str += str[i].upper()
    else:
        converted_str += str[i].lower()

print(converted_str)