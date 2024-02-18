#1. Prepare to read the contents of the file text.txt
#2. Allow the user to enter a parameter "maximum number of characters per line", which must be greater than 35.
#3. Format the text taking into account the maximum number of characters, but if a word does not fit entirely on a line, it should be moved to the next one, and the spacing between words should be evenly increased (similarly to the "Justify" function in text editors). There is a module called ‘textwrap’ which can do it, you may take a look at it but do not use for this task.
#4. Write the resulting text to a new file and notify the user about it.
textFile = open("Task4\\text.txt","r")
fileReadedData = textFile.read()
textFile.close() 

wordsList = fileReadedData.strip().split(' ')
maxWordSize = 0

print(len(wordsList))

for i in range(len(wordsList)):
    if len(wordsList[i]) > maxWordSize:
        maxWordSize = len(wordsList[i])

print(f"Max word lenght:{maxWordSize}")

lineMaximumLenght = 0 
while lineMaximumLenght < maxWordSize:
    lineMaximumLenght = int(input(f"Enter the amount of symbols in the line(N > {maxWordSize}):"))
    if(lineMaximumLenght < maxWordSize):
        print("Error, you character limit is less then biggest word")

textLines = [""]
textLinesIndex = 0
currentLineLimit = lineMaximumLenght

def CheckIfWordWillFitInTheLine(addingWord, lineTargetLenght):
    wordLen = len(addingWord)
    if(wordLen + 1 > lineTargetLenght):
        return False
    else:
        return True

for i in range(len(wordsList)):
    #add check for \n
    #if word have \n in it end, add the word to current line and end it

    if(CheckIfWordWillFitInTheLine(wordsList[i], currentLineLimit)):
        textLines[textLinesIndex] += f"{wordsList[i]} "
        currentLineLimit -= (len(wordsList[i]) + 1)
    else:
        textLines[textLinesIndex] = textLines[textLinesIndex].strip()
        currentLineLimit = lineMaximumLenght
        textLinesIndex += 1
        textLines.append(f"{wordsList[i]} ")
        currentLineLimit -= len(wordsList[i])

def SetLineToStandartLenght(textLine, lineTargetLenght):
    textLineModified = ""
    wordList = textLine.strip().split(' ')

    currentLinesCharacters = len(textLine)

    amountOfAdditionalSpace = (lineTargetLenght - currentLinesCharacters)

    for i in range(len(wordList) - 1):
        wordList[i] = wordList[i] + " "

        if(amountOfAdditionalSpace > 0):
            wordList[i] = wordList[i] + " "
            amountOfAdditionalSpace -= 1
        
    if(amountOfAdditionalSpace > 0):
        wordList[len(wordList) - 1] += " " * amountOfAdditionalSpace

    textLineModified = "".join(str(element) for element in wordList)
    
    print(fr"Check Line:[{textLine}], ModifiedString: [{textLineModified}], lenght:[{currentLinesCharacters}->{len(textLineModified)}], TargetLeght:{lineTargetLenght}")
    textLineModified += "\n"

    return textLineModified

for i in range(len(textLines)):
    textLines[i] = SetLineToStandartLenght(textLines[i], lineMaximumLenght)

def WriteLineListToFile(textLines, maxWordSize):
    croppedFile = open(f"Task4\\text_{maxWordSize}.txt", "w")
    croppedFile.writelines(textLines)
    croppedFile.close()


WriteLineListToFile(textLines, lineMaximumLenght)
    

