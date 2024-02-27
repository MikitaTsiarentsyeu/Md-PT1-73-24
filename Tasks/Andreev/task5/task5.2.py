def reverse_strings(input_list):
  
    return [string[::-1] for string in input_list]
original_strings = input().split()
reversed_strings = reverse_strings(original_strings)
print(reversed_strings)