#5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
#get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#get_ranges([4,7,10])  -> "4, 7, 10"
#get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def getNumberRanges(numberList):
    resultRanges = []
    startRange = endRange = numberList[0]

    for i in range(len(numberList)):
        if(i+1 >= len(numberList)):
            if(startRange != endRange):
                resultRanges.append(f"{startRange}-{endRange}")
            else: 
                resultRanges.append(str(numberList[i]))
            break
        
        if(numberList[i+1] == endRange + 1):
            endRange = numberList[i+1]
        else:
            if(startRange != endRange):
                resultRanges.append(f"{startRange}-{endRange}")
            else: 
                resultRanges.append(str(numberList[i]))

            startRange = endRange = numberList[i+1]

    return ", ".join(resultRanges)

print(f"Example 1: {getNumberRanges([0, 1, 2, 3, 4, 7, 8, 10])}")
print(f"Example 2: {getNumberRanges([0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 15, 16, 18])}")

customNumberList = input("Input your valuablesList by space separator: ").strip().split()
customNumberList = [int(x) for x in customNumberList]
print(getNumberRanges(customNumberList))