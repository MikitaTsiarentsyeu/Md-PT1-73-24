def get_ranges(numbers):
    if not numbers:
        return ""
    
    ranges = []
    start = numbers[0]
    end = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
            start = numbers[i]
            end = numbers[i]
    
    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")
    
    return ", ".join(ranges)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  
print(get_ranges([4, 7, 10]))                 
print(get_ranges([2, 3, 8, 9]))               