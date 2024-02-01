#Write a program that converts kilometers per hour to meters per second, ask a user for the speed.

import math

speed_km_h = int(input("Please, enter the speed in km/h\n"))
speed_m_s = round(speed_km_h * 5 / 18)
print("The speed is", speed_m_s, "m/s")