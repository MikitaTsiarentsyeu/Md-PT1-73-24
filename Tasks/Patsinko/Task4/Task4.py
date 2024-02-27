numb = int(input('Enter the number of symbols - '))

with open('text.txt', 'r') as read_text:
    with open('text_2.txt', 'w') as write_text:
    
        line = read_text.read(numb+1)
        index_position=0
        read_text.seek(index_position)

        while line:
            read_text.seek(index_position)
            line = read_text.read(numb+1)
            
            if line.count('\n') > 0:
                index_move = int(line.index('\n'))+1
                new_line = ''
                for i in line:
                    if len(new_line) < index_move:
                        new_line += i
                new_line = new_line.strip()
                index_position += index_move+1
                write_text.write(new_line+'\n')
                line = read_text.read(index_move)
                
            elif line[-1] != ' ':
                index_move = int(line.rindex(' '))+1
                new_line = ''
                for i in line:
                    if len(new_line) < index_move:
                        new_line += i
                new_line += '\n'
                new_line = new_line.strip()
                for i in new_line:
                    if len(new_line) < numb:
                        new_line = new_line.replace(' ', '  ', numb-len(new_line))
                index_position += index_move
                write_text.write(new_line +'\n')
                line = read_text.read(index_move)
                
            else:
                new_line = line + '\n'
                new_line = new_line.strip()
                write_text.write(new_line+'\n')
                index_position+=len(new_line)+1
            


