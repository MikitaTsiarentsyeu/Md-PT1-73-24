#5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.
removeSymbolsConst = ['.', ',', '?', '!', '(', ')'] 
limitedSymbolsList = []

userData = input("Input your sentance:")
for i in userData:
    if  i in removeSymbolsConst:
        userData = userData.replace(i, '')

wordsList = userData.lower().split(' ')

for i in range(0, len(wordsList)-1):
    if(len(wordsList[i]) > 5):
        limitedSymbolsList.append(wordsList[i])

print(f"Word that are > 5 symbos are: {limitedSymbolsList}")