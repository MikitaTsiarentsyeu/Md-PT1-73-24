'''3. Write a recursive function to count the number of occurrences of a given character in a string.
'''

def find_count(string:str, symb:str):
    count = 0
    if len(string) == 1:
        if string == symb:
            return 1
        else:
            return 0
    else:
        if string[0] == symb:
            count = 1 + find_count(string[1:], symb)
        else:
            count = 0 + find_count(string[1:], symb)
        return count
        
    
s = input('Enter a string:\n') 
symb = input('Enter a symbol that you want to count:\n')
    
print(find_count(s, symb))  
  