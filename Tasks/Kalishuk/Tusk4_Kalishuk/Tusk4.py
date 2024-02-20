with open('text.txt', 'r') as file:
    text = file.read()

max_chars = int(input("Введите максимальное количество символов в строке (больше 40): "))
while max_chars <= 35:
    max_chars = int(input("Введите максимальное количество символов в строке (больше 40): "))

formatted_text = ""

area = ""
for paragraph in text.split("\n"):
    lines = paragraph.split("\n")
    for line in lines:
        words = line.split()
        
        for word in words:
            if len(area + word) <= max_chars:
                area += word + " "
            else:
                spaces_to_add = max_chars - len(area) +1
                words_in_area = area.split()
                if len(words_in_area) > 1:
                    avg_spaces = spaces_to_add // (len(words_in_area) - 1)
                    extra_spaces = spaces_to_add % (len(words_in_area) - 1)
                    for i in range(len(words_in_area) - 1):
                        words_in_area[i] += " " * avg_spaces
                        if extra_spaces > 0:
                            words_in_area[i] += " "
                            extra_spaces -= 1
                formatted_text += ' '.join(words_in_area) + '\n'
                area = word + " "
    if area:
        formatted_text += area + '\n'
        area=""    

# print(formatted_text)

# Запись в новый файл
with open('formatted_text.txt', 'w', encoding='utf-8') as file:
    file.write(formatted_text)

print("The formatted text has been saved to formatted_text.txt")