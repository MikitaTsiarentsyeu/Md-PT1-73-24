def count_char_recursive(s, char):

    if not s:
        return 0
    elif s[0] == char:
        return 1 + count_char_recursive(s[1:], char)
    else:
        return count_char_recursive(s[1:], char)


input_string = input("Your text: ")
target_char = input("You simbol: ")
result = count_char_recursive(input_string, target_char)
print(f"Количество вхождений символа '{target_char}' в строку: {result}")
