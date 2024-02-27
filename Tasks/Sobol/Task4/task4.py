import os
width = int(input("Input width value: "))
if (width < 35):
    print("Input value more or equal 35")
    exit()
os.chdir('C:\PythonProj\Task4')
with open("text.txt", "r") as file:
    text = file.read()
    text_ok = ""
    paragrafs = text.split('\n')
    for paragraf in paragrafs:
        line = ""
        line_end = 0
        words = paragraf.split()
        for word in words:
            if (line_end + len(word) < width):
                line += word + ' '
                line_end += len(word) + 1
            else:
                if (line_end + len(word) == width):
                    line += word
                else:
                    k_space = width - line_end + 1
                    k_inst = len(line.split()) - 1
                    chast = k_space // k_inst
                    ost = k_space % k_inst
                    line1 = ''
                    for word1 in line.split():
                        line1 += word1 + ' '
                        if k_inst > 0:
                            line1 += ' ' * chast
                            k_inst -= 1
                        if ost > 0:
                            line1 += ' '
                            ost -= 1
                    line = line1        
                text_ok += line + '\n'
                line = word + ' '
                line_end = len(line)
        text_ok += line + '\n'        
    text = text_ok
with open('f_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("The formatted text has been saved to formatted_text.txt")              