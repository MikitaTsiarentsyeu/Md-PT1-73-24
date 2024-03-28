text  = input("Enter the value of vowels:\n")

list_vowels = ['a','e','i','o','u']
count = ''

for i in text:
    if i in list_vowels:
        continue
    else:
        count += i
print(count)