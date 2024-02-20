list_strings = ["Marco", "Harry", "Ronn", "Alison", "Lisa", "Marc", "Luda", "Chris", "Eva", "Anna", "Tomas", "Dzmitry"]

list_5more_characters = []
for i in list_strings:
    if len(i) > 5:
        list_5more_characters.append(i)
print(list_5more_characters)