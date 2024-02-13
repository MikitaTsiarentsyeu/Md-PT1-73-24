string = input("Input string:")
count = 0
vowels = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y')
for letter in string:
    if letter in vowels:
        count += 1
print("Count of vowels =:")
print(count)
      