def reverse_string(input_string):
    reversed_string = ""
    for char in reversed(input_string):
        reversed_string += char
    return reversed_string

user_input = input("Введите строку:")
reversed_input = reverse_string(user_input)
print("Строка в обратном порядке:", reversed_input)