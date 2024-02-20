input_numbers = [23, 32, 55, 0, 7, 6, 17, 9, 4, 19]
Average = round(sum(input_numbers)/len(input_numbers))
print("The average of all numbers is", Average)
Summ = 0
for i in range(len(input_numbers)):
    Summ += input_numbers[i]
print("The average of all numbers is", round(Summ / len(input_numbers)))