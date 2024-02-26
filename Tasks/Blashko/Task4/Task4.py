
# добавить пробелы в строку
def add_spaces(user_input:int, string:str):
    
        while len(string) < user_input:
            string = string.replace(' ', '  ', (user_input-len(string)))
        return string

      
# форматировать параграф
def format_paragraph(len_string:int, string:str): 
    len_string = len_string - 1   # чтобы не учитывать в финальной строке символ '\n'
    list_string = string.split()
    paragraf = []
    new_str = ''
          
    for word in list_string:
        if new_str == '':
            new_str += word         
        else:
            if len(new_str + ' ' + word) < len_string:
                new_str += ' ' + word
                if word == list_string[-1]:
                    new_str += '\n'
                    paragraf.append(new_str)
                    new_str = ''
                    
            elif len(new_str + ' ' + word) == len_string:
                new_str += ' ' + word + '\n'
                paragraf.append(new_str)
                new_str = ''
                
            elif len(new_str + ' ' + word) > len_string:
                new_str += '\n'
                paragraf.append(add_spaces(len_string+1,new_str))
                new_str = word
            
    if new_str != '':
        new_str += '\n'   
        paragraf.append(new_str)
                
    return len_string, paragraf

    
    
# получить список параграфов из файла
list_paragraf = []

with open('text.txt', 'r') as file:
    for paragraf in file.readlines():
        list_paragraf.append(paragraf)
   
   
 
# пользовательский ввод    
while True:
    user_input = input("Please enter the maximum number of characters per line, which must be greater than 35.: ")
    if user_input.isdigit():
        if int(user_input) >35:
            user_input = int(user_input)
            break
        else:
            print("It must be greater then 35\n")
    else:
        print("It must be digit\n")
    
       
# запись в файл отформатированного текста   
with open(f'to_{user_input}_format.txt', 'a+') as file:
    for paragraf in list_paragraf:
        file.writelines(format_paragraph(user_input,paragraf)[1])
    print('Formatting done!')
    print(f'Open to_{user_input}_format.txt file to see the formatted text')
