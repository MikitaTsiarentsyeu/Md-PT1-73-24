"5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters."

string = input('Enter the list in the format: one two three : \n')
string = list(string.split(' '))
st = [i for i in s if len(i)>5]
print(st)