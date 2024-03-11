def countLetterString(char, str, count = 0):
    if len(str) == 0:
        return count
    if str[-1] == char:
        return countLetterString(char, str[0:-1], count+1)
    else:
        return countLetterString(char, str[0:-1], count)

str = "London is the capital of Great Britain"
char = "t"
print(countLetterString(char, str)) 