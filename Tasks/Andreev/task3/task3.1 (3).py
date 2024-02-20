input_string = input("Введи свой текст:")
word_counts = {}
for word in input_string.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)
