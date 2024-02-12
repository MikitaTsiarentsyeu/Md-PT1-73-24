input_string = input("Please enter text here\n")

vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']

new_string = ''
for i in input_string:
    if i in vowel_list:
        continue
    else:
        new_string += i
print(new_string)