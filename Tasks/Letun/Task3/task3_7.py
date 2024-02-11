def reverse_case(string):
    reversed_string = ""
    for char in string:
        if char.islower():
            reversed_string += char.upper()
        elif char.isupper():
            reversed_string += char.lower()
        else:
            reversed_string += char
    return reversed_string
    
input_string = input("Введите строку: ")
reversed_case_string = reverse_case(input_string)
print("Результат:", reversed_case_string)
