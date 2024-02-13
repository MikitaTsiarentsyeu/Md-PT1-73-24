#7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa
userData = input("Input your sentance:")
changedString = ""

for i in range(0, len(userData)-1):
    if userData[i].islower():
        changedString += userData[i].upper()
    else:
        changedString += userData[i].lower()

print(f"Changed string: {changedString}")