def rec_fibonacci(n:int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return rec_fibonacci(n-2) + rec_fibonacci(n-1)


number = int(input('Enter a number: \n'))
print(f'Tne {number}th in the Fibonacci sequence is - {rec_fibonacci(number)}')