# 2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

input_numbers = [6, 2, 4, 1, 77, 33]

total = 0
for i in input_numbers:
    if i % 2 == 0:
        total += i
print("The sum of all even numbers is", total)
