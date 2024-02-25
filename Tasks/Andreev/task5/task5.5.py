def get_ranges(numbers):
   
    if not numbers:
        return ""

    result = []
    start_range = end_range = numbers[0]

    for num in numbers[1:]:
        if num == end_range + 1:
            end_range = num
        else:
            if start_range == end_range:
                result.append(str(start_range))
            else:
                result.append(f"{start_range}-{end_range}")
            start_range = end_range = num

    
    if start_range == end_range:
        result.append(str(start_range))
    else:
        result.append(f"{start_range}-{end_range}")

    return ", ".join(result)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  # Output: "0-4, 7-8, 10"
print(get_ranges([4, 7, 10]))  # Output: "4, 7, 10"
print(get_ranges([2, 3, 8, 9]))  # Output: "2-3, 8-9"