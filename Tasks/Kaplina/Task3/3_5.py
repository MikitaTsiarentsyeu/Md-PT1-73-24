# 5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.

list_strings = ["Kai", "Liam", "Noah", "Mia", "Eliana", "Mila", "Luca", "Charlotte", "Nova", "Ava", "James", "Aurelia"]

list_5more_characters = []
for i in list_strings:
    if len(i) > 5:
        list_5more_characters.append(i)
print(list_5more_characters)




