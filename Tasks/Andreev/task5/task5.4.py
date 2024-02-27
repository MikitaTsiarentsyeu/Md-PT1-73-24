def my_count(input_string):
    
    lower_count = 0
    upper_count = 0

    for char in input_string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1

    return lower_count, upper_count

sample_string = input("введи свой текст: ")
lower, upper = my_count(sample_string)
print(f"Lowercase count: {lower}")
print(f"Uppercase count: {upper}")