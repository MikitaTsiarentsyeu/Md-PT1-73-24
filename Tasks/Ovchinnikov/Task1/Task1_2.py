#Calculate area of circle by radius
import math

circle_radius = input("Radius of circle is: \n")
circle_area = math.pi * (float(circle_radius) ** 2)

print(f"Area of provided circle is: {circle_area}")