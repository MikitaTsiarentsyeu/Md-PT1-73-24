n = int(input('Enter which Fibonacci number you want to find out:\n'))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(f'The {n}th Fibonacci numbers are {fibonacci(n)}')
