def sum_even_numbers(numbers):
    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
    return sum_even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers)
print("Сумма четных чисел:", result)