# 2. Write a recursive function to check whether a given string is a palindrome.

def PalindromeCheckRecur(checkString):
    if(len(checkString) <= 1):
        return True

    if(checkString[0] == checkString[-1]):
        return PalindromeCheckRecur(checkString[1:-1])
    else:
        return False
    
def ReverseStringRecur(nonReversedString):
    global reversedString
    if(len(nonReversedString) <= 0):
        return reversedString

    reversedString += nonReversedString[-1]
    nonReversedString = nonReversedString[:-1]

    return ReverseStringRecur(nonReversedString)
        
userData = input("Enter your string: ")
userData = userData.strip().lower().replace(" ", "")
reversedString = ""
reversedString = ReverseStringRecur(userData)

if(PalindromeCheckRecur(userData)):
    print(f"Your string is Polindrom, Reversed: {userData} -> {reversedString}")
else:
    print(f"Your string isn't Polindrome, Reversed: {userData} -> {reversedString}")