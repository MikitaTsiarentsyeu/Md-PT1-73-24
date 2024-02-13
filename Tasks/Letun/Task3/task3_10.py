def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_largest_prime(numbers):
    largest_prime = None
    for num in numbers:
        if is_prime(num) and (largest_prime is None or num > largest_prime):
            largest_prime = num
    return largest_prime

numbers = [1, 3, 5, 7, 4, 9, 11, 2, 6]
largest_prime = get_largest_prime(numbers)
print(largest_prime)  