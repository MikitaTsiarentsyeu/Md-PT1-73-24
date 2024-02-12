'10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.'
list_n = input('Enter the list in the format: 1 21 35 4 : \n')
n = list(list_n.split(' '))

k=[]
for j in n:
    for i in range(2, int(j)):
        if int(j)%i != 0:
            break 
    else:
        k.append(j)
print(k)



    