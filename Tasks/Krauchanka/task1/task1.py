
Celsius= float(input("Введите значение в градусах по Цельсию: "))
Fahrenheit = Celsius*9/5+32
print ("Fahrenheit: ", Fahrenheit)

R= float (input("ВВедите значение радиуса, R= "))
PI=3.14
S= R**2*PI
print ("Площадь круга равна ", S)

V_km_m= float(input("Введите скорость в километрах в час: "))
V_m_s= V_km_m*1000/3600
print ("Cкорость ", V_m_s, "м/c")

USA= float (input("ВВедите сумму в долларах США  "))
Exchange=3.16
BYN=USA*Exchange
print ("BYN ", BYN)

import random
left=int(input("Введите левую границу: "))
right=int(input("Введите правую границу: "))
a=random.randint(left,right)
print (a)