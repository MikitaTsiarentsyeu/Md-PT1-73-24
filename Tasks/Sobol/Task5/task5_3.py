def words_greater_than_5(lst):
    long_words = []
    for word in lst:
        if len(word) >= 5:
                long_words.append(word)
    return long_words
print(words_greater_than_5(list(map(str, input("Input values: ").split()))))            