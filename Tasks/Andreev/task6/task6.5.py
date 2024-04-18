def fibonacci_recursive(n):
  
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


position = int(input("Inter number_position: ")) 
result = fibonacci_recursive(position)
print(f"The {position}th Fibonacci number is: {result}")
