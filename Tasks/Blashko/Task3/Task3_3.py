"""3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
"""

# получаем ввод от пользователя
string = input('Enter string:\n')

# задаем список символов, которые хотим удалить из строки
symb = ['.', ',', ':', ';', '?', '!', '-', '_', '(', ')', '@', '"', "'"] 

# избавляемся от ненужных символов
for i in string:
    if i in symb:
        string = string.replace(i, '')
        
# получаем список слов
list_string = string.lower().split()

# создаем и заполняем словарь словами из списка и ведем подсчет колличества слов
d = {word:count for word, count in zip(list_string, [list_string.count(i) for i in list_string])}

              
# выводим на экран полученный словарь   
for key, value in sorted(d.items(), key=lambda value: value[1], reverse=True):
    print(f'{value}: {key}', end='\n')

