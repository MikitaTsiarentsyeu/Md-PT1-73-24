time_input = input("Введите время в формате чч:мм: ")

hours, min = time_input.split(":")
hours = int(hours)
min = int(min)

output = ""

if min == 0:
    output = f"такое-то значение часов ровно ({hours}:00 - {hours} часов ровно)"
elif min < 30:
    output = f"столько-то минут ({hours}:{min:02d} - {min} минут {hours + 1}:00 - го)"
elif min == 30:
    output = f"половина такого-то ({hours}:{min:02d} - половина {hours + 1}:00 - го)"
elif min > 30 and min < 45:
    output = f"столько-то минут ({hours}:{min:02d} - {min} минут {hours + 1}:00 - го)"
else:
    output = f"без {60 - min} такого-то ({hours}:{min:02d} - без {60 - min} минут {hours + 1}:00 - го)"

print(output)