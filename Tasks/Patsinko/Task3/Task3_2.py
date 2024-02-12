"2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list."
list_n = input('Enter the list in the format: 1 21 35 4 : \n')
l = list(list_n.split(' '))
sum_even = 0
for i in l:
    if int(i)%2 != 0:
        continue
    sum_even += int(i)
print(sum_even)