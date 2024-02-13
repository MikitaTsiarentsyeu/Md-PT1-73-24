str = input("Input string:")
counts = dict()
words = str.split()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print("Counts: ", counts)            