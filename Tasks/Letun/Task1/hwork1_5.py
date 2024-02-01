#5.Write a program that generates a random number in a given range, and shows the answer to a user, ask a user for the left and right border.

import random

# Запрос левой границы у пользователя
left_boundary = int(input("Введите левую границу диапазона: "))

# Запрос правой границы у пользователя
right_boundary = int(input("Введите правую границу диапазона: "))

# Генерация случайного числа в заданном диапазоне
random_number = random.randint(left_boundary, right_boundary)

# Вывод сгенерированного числа
print(f"Случайное число в диапазоне от {left_boundary} до {right_boundary}: {random_number}")