input_filename = "text.txt"
with open(input_filename, "r") as input_file:
    original_text = input_file.read()


while True:
    try:
        max_line_length = int(input("Enter the maximum number of characters per line (greater than 35): "))
        if max_line_length <= 35:
            print("Please enter a value greater than 35.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


words = original_text.split()
formatted_text = ""
area = ""
for paragraph in original_text.split("\n"):
    lines = paragraph.split("\n")
    for line in lines:
        words = line.split()
        
        for word in words:
            if len(area + word) <= max_line_length:
                area += word + " "
            else:
                spaces_to_add = max_line_length - len(area) +1
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
output_filename = "formatted_text.txt"
with open(output_filename, "w") as output_file:
    output_file.write(formatted_text)

print(f"Formatted text has been written to {output_filename}.")        