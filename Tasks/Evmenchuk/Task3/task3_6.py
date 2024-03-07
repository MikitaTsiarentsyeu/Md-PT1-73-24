str_input = input("Enter your string: \n").casefold()

vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']

vowels_remove = ''
for i in str_input:
    if i in vowel_list:
        continue
    else:
        vowels_remove += i
print(vowels_remove)
