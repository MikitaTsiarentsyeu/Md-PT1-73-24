"3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string."
string = input('Enter the string: \n')
sings = [',', '.', '!', '?', ':', ';']
for i in string:
    if i in sings:
        string = string.replace(i, '')
d = {}
string = string.split(' ')
for i in string:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
