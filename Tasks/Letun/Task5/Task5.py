# 1. Write a function that takes two integers as arguments and returns their sum.

def calculate_sum(num1, num2):
    return num1 + num2

result = calculate_sum(3, 5)
print(result) 


# 2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.

def reverse_strings(strings):

  reversed_strings = []
  for string in strings:
    reversed_strings.append(string[::-1])

  return reversed_strings

strings = ["Hello", "World", "How", "Are", "You"]
reversed_strings = reverse_strings(strings)
print(reversed_strings)  


# 3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

def filter_long_strings(strings):

  long_strings = []
  for string in strings:
    if len(string) > 5:
      long_strings.append(string)

  return long_strings

strings = ["Hello", "World", "How", "Are", "PSV", "Liverpool"]
long_strings = filter_long_strings(strings)
print(long_strings) 


# 4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, 
# second for count of the upper case letters in the initial string.

def count_letters(input_string):
    lowercase_count = 0
    uppercase_count = 0

    for char in input_string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1

    return lowercase_count, uppercase_count

input_string = "Hello, World!"
lowercase_count, uppercase_count = count_letters(input_string)
print(lowercase_count, uppercase_count)


# 5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
#    get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#    get_ranges([4,7,10])  -> "4, 7, 10"
#    get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def get_ranges(nums):
    ranges = []
    start = end = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            end = nums[i]
        else:
            ranges.append(str(start) if start == end else f"{start}-{end}")
            start = end = nums[i]
    
    ranges.append(str(start) if start == end else f"{start}-{end}")
    
    return ', '.join(ranges)

# Test cases
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  # Output: "0-4, 7-8, 10"
print(get_ranges([4, 7, 10]))  # Output: "4, 7, 10"
print(get_ranges([2, 3, 8, 9]))  # Output: "2-3, 8-9"


