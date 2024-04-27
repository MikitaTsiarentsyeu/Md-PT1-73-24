while True:
    line_lenght = input(
        '\nEnter the numbers of symbols in the line (more than 35):')
    if line_lenght.isdigit() and int(line_lenght) > 35:
        line_lenght = int(line_lenght)
        break
    else:
        print('INPUT ERROR: Invalid string length')

with open('text.txt', 'r', encoding='utf-8') as text, open('formatted_text.txt', 'w', encoding='utf-8') as new_text:

    line = text.readline()

    while line != '':
        while len(line) > line_lenght:
            end = line.rfind(' ', 0, line_lenght)

            if end != line_lenght:
                new_line = line[:end]
            else:
                line[:line_lenght]

            if end != line_lenght:
                line = line[end+1:]
            else:
                line[line_lenght+1:]
            required = line_lenght-len(new_line)-1
            exist = new_line.count(' ')
            count = 2
            while len(new_line) != line_lenght-1:
                if required <= exist:
                    new_line = new_line.replace(
                        ' ' * (count - 1), ' ' * count, required)
                else:
                    new_line = new_line.replace(
                        ' ' * (count - 1), ' ' * count, exist)

                    count += 1
                    required -= exist
            new_text.write(new_line + '\n')
        new_text.write(line)
        line = text.readline()
