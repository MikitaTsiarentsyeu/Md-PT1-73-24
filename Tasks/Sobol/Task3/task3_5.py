lst = list(map(str, input("Input values: ").split()))
long_words = []
for word in lst:
    if len(word) >= 5:
            long_words.append(word)
print("Words with length greater than 5 characters" ,long_words)