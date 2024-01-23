import random

print("Enter the left and right range")
left_range = int(input("Input the left range:"))
right_range = int(input("Input the right range:"))
random_number = random.randrange(left_range, right_range + 1)
print("Our random number is :", random_number)