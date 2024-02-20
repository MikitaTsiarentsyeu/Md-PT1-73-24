input_numbers = [23, 32, 55, 0, 7, 6, 17, 9, 4, 19]

max = 0
for i in input_numbers:
    if i > 1:
        for n in range(2, i // 2 + 1):
            if i % n == 0:
                break
        else:
            if i> max:
                max = i

if max == 0:
    print("No prime numbers in the list")
else:
    print("The largest prime number is", max)