#3.Write a program that converts kilometers per hour to meters per second, ask a user for the speed.

kmph = float(input("Enter speed in Km/Hr: "))
mps = (kmph * 1000)/3600
print("The speed in m/s is",round(mps,2))