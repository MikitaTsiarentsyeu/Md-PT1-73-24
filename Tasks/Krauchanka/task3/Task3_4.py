# Write a program that takes a list of numbers as input and 
# returns the second largest number in the list.

number = list(input('Enter numbers separated by space: ').split())

for x in range(len(number)-1):
    for i in range(len(number)-1):
        if number[i] > number[i+1]:
            number[i], number[i+1] = number[i+1], number[i]
            

print("The second largest number is : ",number[-2])