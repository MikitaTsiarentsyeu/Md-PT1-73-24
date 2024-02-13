# 3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.

input_string = input("Please enter text here\n")

new_string = ''
for i in input_string:
    if i in ',!?.:;-_()':
        continue
    new_string += i

new_string_words = new_string.split()

dict_words={}
for word in new_string_words:
    dict_words[word] = dict_words.get(word, 0)+1

print(dict_words)
