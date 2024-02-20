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
current_line = ""


for word in words:
   
    if len(current_line) + len(word) + 1 > max_line_length:
        formatted_text += current_line.strip() + "\n"
        current_line = ""
 
    current_line +=  word + " "

if current_line:
    formatted_text += current_line.strip()


output_filename = "formatted_text.txt"
with open(output_filename, "w") as output_file:
    output_file.write(formatted_text)

print(f"Formatted text has been written to {output_filename}.")