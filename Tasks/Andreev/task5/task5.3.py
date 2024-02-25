def filter_long_strings(input_list):
    
    return [string for string in input_list if len(string) > 5]

original_strings = input().split()
filtered_strings = filter_long_strings(original_strings)
print(filtered_strings)