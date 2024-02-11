def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
average = calculate_average(numbers)
print("Average:", average)