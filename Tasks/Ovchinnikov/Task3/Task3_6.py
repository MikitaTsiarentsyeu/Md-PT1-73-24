#6. Write a program that takes a string as input and returns the string with all vowels removed.
vowelsConst = ['a', 'e', 'i', 'o', 'u', 'y']

userData = input("Input your word:")

for i in range(0, len(userData)-1):
    if userData[i] in vowelsConst:
        userData = userData.replace(userData[i], '')

print(f"Your word without vowels: {userData}")