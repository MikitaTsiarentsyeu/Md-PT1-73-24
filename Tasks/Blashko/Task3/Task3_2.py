"""2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list."""

try:
    numbers = list(map(int, input('Enter numbers separated by space:\n').split()))
    list_even = [x for x in numbers if x % 2 == 0]
    print(f'Your numbers: {numbers}')
    print(f'Sum of all even numbers in the list: {sum(list_even)}')
except ValueError:
    print('incorrect input')
