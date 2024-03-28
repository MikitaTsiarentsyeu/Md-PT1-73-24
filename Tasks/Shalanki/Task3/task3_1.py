text  = input("Enter the value of vowels:\n")

count = 0

for charakters in text:
    if (charakters in "aAeEiIoOuU"):
        count += 1

print("Count:", count)