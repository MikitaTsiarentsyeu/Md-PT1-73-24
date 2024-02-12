input_string = input("Please enter text here\n")

vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']

vowel_count = 0
for i in input_string:
    if i in vowel_list:
        vowel_count +=1
print("Number of vowels:", vowel_count)