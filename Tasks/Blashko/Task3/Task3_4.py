"""4. Write a program that takes a list of numbers as input and returns the second largest number in the list.
"""

numbers = list(map(int, input('Enter numbers separated by space:\n').split()))

for k in range(len(numbers)-1):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            

print(f'The second largest number in the list is : {numbers[-2]}')


