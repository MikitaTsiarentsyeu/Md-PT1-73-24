# 10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.


input_numbers = [-22, 0, 22, 293, 71, 3, 6, 7, 8, 9, 11, 23, 37, 277]

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

