str_input = input("Enter your string: \n").casefold()

vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']

vowel_count = 0
for i in str_input:
    if i in vowel_list:
        vowel_count += 1
print("Number of vowels:", vowel_count)
