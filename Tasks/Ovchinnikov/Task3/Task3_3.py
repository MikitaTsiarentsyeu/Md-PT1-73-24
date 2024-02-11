#3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
removeSymbolsConst = ['.', ',', '?', '!', '(', ')'] 
wordCountDictionary = {}

userData = input("Input your sentance:")
for i in userData:
    if  i in removeSymbolsConst:
        userData = userData.replace(i, '')

wordsList = userData.lower().split(' ')

for i in range(0, len(wordsList)-1):
    if wordsList[i] in wordCountDictionary.keys():
        wordCountDictionary[wordsList[i]] += 1
    else:
        wordCountDictionary[wordsList[i]] = 1

print(f"Word count in your sentance: { list(wordCountDictionary.items())}")