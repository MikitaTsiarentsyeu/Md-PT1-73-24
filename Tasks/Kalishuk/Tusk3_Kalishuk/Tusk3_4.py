input_numbers = [22, 105, 0, 44, 5, 6, 7, 1, 2, 39]

max = input_numbers[0]
second_max = 0
for i in input_numbers:
    if i > max:
        second_max = max
        max = i
    if i > second_max and i < max:
        second_max = i
print(second_max)