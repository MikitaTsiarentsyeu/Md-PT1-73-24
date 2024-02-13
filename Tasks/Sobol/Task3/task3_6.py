string = input("Input string:")
result = ""
vowels = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y')
for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]
print("String after removing vowels:", result)        