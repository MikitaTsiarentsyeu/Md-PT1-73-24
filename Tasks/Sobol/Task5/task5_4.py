def upper_and_lower_letters(str):
    uppercase_letters = 0
    lowercase_letters = 0
    for i in str:
        if i.isupper():
            uppercase_letters += 1
        else:
            lowercase_letters += 1
    return uppercase_letters,  lowercase_letters  
print(upper_and_lower_letters(input("Input string: ")))    