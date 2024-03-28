'''5. Write a recursive function to find the Nth number in the Fibonacci sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21

n = 6 => 5'''


def rec_fibonacci(n:int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return rec_fibonacci(n-2) + rec_fibonacci(n-1)


number = int(input('Enter a number: \n'))
print(f'Tne {number}th in the Fibonacci sequence is - {rec_fibonacci(number)}')
    