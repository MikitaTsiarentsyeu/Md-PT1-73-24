def find_second_largest(numbers):
    
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        
        if num > largest:
            second_largest = largest
            largest = num
        
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


numbers = [9, 2, 7, 5, 1, 6]
second_largest_number = find_second_largest(numbers)
print(f"Второе по величине число: {second_largest_number}")