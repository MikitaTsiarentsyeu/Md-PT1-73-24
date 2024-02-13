str = input("Input string:")
swapped = ""
for i in str:
    if(i.isupper()):
        swapped += i.lower()
    else:
        swapped += i.upper()
print(swapped)            