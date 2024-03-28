# 5. Write a recursive function to find the Nth number in the Fibonacci sequence.

# 0, 1, 1, 2, 3, 5, 8, 13, 21
# n = 6 => 5

# Var #1
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))
print(Fibonacci(7))


# Var #2
saved = {}
def Fibonacci(n):
    if n in saved:
        return saved[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = Fibonacci(n-1) + Fibonacci(n-2)
        saved[n] = result
        return result

print(Fibonacci(7))