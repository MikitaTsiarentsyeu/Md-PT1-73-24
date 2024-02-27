# Write a recursive function to check whether a given string is a palindrome.
# Палиндро́м — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях.

def palindrome (string):
    string = string.lower().replace(" ","")
    if len (string) <=1:
        return True
    else:
        if string[0] == string[-1]:  
            return palindrome(string[1:-1])
        else:
            return False

print (palindrome ("Madam"))
print (palindrome ("Was it a car or a cat I saw"))
print (palindrome ("Level"))
print (palindrome ("function"))
print (palindrome ("2"))


