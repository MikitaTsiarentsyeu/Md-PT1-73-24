'8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.'
line_n = input('Enter the list in the format: 1 21 35 4 : \n')
n = list(line_n.split(' '))
t=0
for i in n:
    t += int(i)
avarg = round(t/len(n),2)
print(avarg)