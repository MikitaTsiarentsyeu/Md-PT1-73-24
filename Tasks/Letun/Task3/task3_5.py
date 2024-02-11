def filter_strings(strings):
    result = []
    for string in strings:
        if len(string) > 5:
            result.append(string)
    return result

input_strings = ["apple", "orange", "banana", "kiwi", "mango"]
filtered_strings = filter_strings(input_strings)
print(filtered_strings)
