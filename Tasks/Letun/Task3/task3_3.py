def count_words(sentence):
    word_count = {}

    for word in sentence.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

input_string = input("Введите строку: ")

result = count_words(input_string)
print(result)