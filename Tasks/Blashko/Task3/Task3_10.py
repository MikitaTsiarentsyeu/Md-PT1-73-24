"""10. Write a program that takes a list of numbers as input and returns the largest prime number in the list."""

list_numbers = [-15, -7,  -1, 1, 2, 7, 8, 10, 15, 107, 109, 113, 127, 131, 139, 149, 151, 200, 220, 250]
list_prime = []

for number in list_numbers:
    if number > 0 and number !=1:
        for x in range(2, number):
            if number % x == 0:
                break
        else:
            list_prime.append(number)


if len(list_prime):    
    print(f'Largest prime number is - {max(list_prime)}')   
else:          
    print("Prime number is not in list")
