input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

sum_even = 0
for i in input_numbers:
    if i % 2 == 0:
        sum_even += i

print(sum_even)
