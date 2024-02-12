input_numbers = [12, 2, 18, 1, 66, 33]

total = 0
for i in input_numbers:
    if i % 2 == 0:
        total += i
print("The sum of all even numbers is", total)