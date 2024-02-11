# 8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list

input_numbers = [-22, 77, 9, 0, 55, 11, 2, 3, 5, 7]
# Case 1
Average = round(sum(input_numbers)/len(input_numbers))
print("The average of all numbers is", Average)


# Case 2
Summ = 0
for i in range(len(input_numbers)):
    Summ += input_numbers[i]
print("The average of all numbers is", round(Summ / len(input_numbers)))


