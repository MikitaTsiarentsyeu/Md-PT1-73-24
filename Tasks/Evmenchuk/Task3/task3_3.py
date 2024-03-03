remove_symbols = ['.', ',', '!', '?', ':', ';', '(', ')']

input_string = input("Enter your sentence: \n")

for i in input_string:
    if i in remove_symbols:
        input_string = input_string.replace(i, '')

string_list = input_string.lower().split()

words_dict = {}

for word in string_list:
    words_dict[word] = words_dict.get(word, 0)+1
print(words_dict)
