#Implement a text output of the time entered from the console (the user should input data in the format hh:mm).

#Show the responses to the user in Russian according to the rules listed below:

#min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
#min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
#min == 30: половина такого-то (15:30 - половина четвёртого)
#min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
#min >= 45 без min такого-то (08:54 - без шести минут девять)

time_input = input("Введите время в формате чч:мм: ")

# Разделяем время на часы и минуты
hours, minutes = time_input.split(":")
hours = int(hours)
minutes = int(minutes)

output = ""

# Проверяем условия и формируем текстовый вывод
if minutes == 0:
    output = f"такое-то значение часов ровно ({hours}:00 - {hours} часов ровно)"
elif minutes < 30:
    output = f"столько-то минут ({hours}:{minutes:02d} - {minutes} минут {hours + 1}:00 - го)"
elif minutes == 30:
    output = f"половина такого-то ({hours}:{minutes:02d} - половина {hours + 1}:00 - го)"
elif minutes > 30 and minutes < 45:
    output = f"столько-то минут ({hours}:{minutes:02d} - {minutes} минут {hours + 1}:00 - го)"
else:
    output = f"без {60 - minutes} такого-то ({hours}:{minutes:02d} - без {60 - minutes} минут {hours + 1}:00 - го)"

print(output)


