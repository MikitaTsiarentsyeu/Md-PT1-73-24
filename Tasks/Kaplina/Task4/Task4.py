
characters_per_line = int(input("Please enter maximum number of characters per line, greater than 35\n"))

if characters_per_line <= 35:
        print("This value is less or equal to 35")


with open('text.txt', 'r') as f:
    text = f.read()

paragraphs = text.split('.\n')
formatted_paragraphs = []

for paragraph in paragraphs:
    words = paragraph.split() 
    lines = []
    current_line = []

    while words: 
        while words and len(' '.join(current_line + [words[0]])) <= characters_per_line:
            current_line.append(words.pop(0))

        if words:  
            while len(' '.join(current_line)) < characters_per_line:
                for i in range(len(current_line) - 1):
                    if len(' '.join(current_line)) < characters_per_line:
                        current_line[i] += ' '
                    else:
                        break
        lines.append(' '.join(current_line))
        current_line = []

    formatted_paragraphs.append('\n'.join(lines))

formatted_text = '.\n'.join(formatted_paragraphs)

with open('formatted_text.txt', 'w') as f:
    text = f.write(formatted_text)
print("Please find formatted text with a given number of characters per line in a separate file 'formatted_text.txt'")