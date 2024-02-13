# 3. Write a program that takes a string as input and returns a dictionary 
# with the count of each word in the string.

string= list(input ("enter text: "))
d= {}
for c in string:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
print (d)

