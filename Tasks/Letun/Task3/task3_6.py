def remove_vowels(input_string):
    vowels = set('aeiouAEIOU')

    filtered_string = ''
    for char in input_string:
        if char not in vowels:
            filtered_string += char

    return filtered_string

input_string = input("Введите строку: ")

result = remove_vowels(input_string)
print(result)