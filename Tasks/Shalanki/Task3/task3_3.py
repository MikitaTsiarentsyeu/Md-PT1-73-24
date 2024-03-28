str = input("London is the capital of Great Britain:\n")

str = str.replace(',', '').lower().split()

d = {}

for word in str:
    if word in d.keys():
        d[word] += 1 
    else:
        d[word] = 1

print(d)