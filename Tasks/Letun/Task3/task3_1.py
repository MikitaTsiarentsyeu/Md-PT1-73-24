def count_vowels(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
result = count_vowels(user_input)
print("Number of vowels:", result)