"""8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list."""

list_numbers = list(map(float, input('Enter list of numbers:\n').split()))    

summ = 0
for number in list_numbers:
    summ += number
    
average = summ/len(list_numbers)

print(f'Average of all input numbers is: {average}')