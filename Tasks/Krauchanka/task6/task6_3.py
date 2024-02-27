# 3. Write a recursive function to count the number of occurrences of a given character in a string.

def count_number (string, meaning):
    if len(string)==0:
        return 0
    elif string[0]==meaning:
        return 1+ count_number (string[1:], meaning)
    else:
        return count_number (string[1:], meaning)

string = "Have a good day"
meaning = "a"
print (count_number(string, meaning))
