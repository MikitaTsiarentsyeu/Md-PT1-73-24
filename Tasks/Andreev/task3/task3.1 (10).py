input_numbers = input().split()
for i in range(len(input_numbers)):
    input_numbers[i] = int(input_numbers[i])
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