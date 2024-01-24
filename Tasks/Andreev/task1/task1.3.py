#Write a program that converts kilometers per hour to meters per second, ask a user for the speed.
kmph= float(input("Введите скорость в Km/Hr: "))

mps = (kmph * 1000)/3600
print("Скорость в m/s равна: ",round(mps,2))