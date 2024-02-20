s = input("Enter a string: ")
result =""
for char in s:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()
print("String with swapped case ", result)
