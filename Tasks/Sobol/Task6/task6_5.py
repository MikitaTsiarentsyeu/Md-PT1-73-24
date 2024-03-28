def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
n = int(input("Input n: "))
result = fibonacci(n-1)
print(result)