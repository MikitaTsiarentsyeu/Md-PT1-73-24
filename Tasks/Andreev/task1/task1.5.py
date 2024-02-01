#Write a program that generates a random number in a given range, and shows the answer to a user, ask a user for the left and right border.
import random
 

l = int(input("ВВеди низ: "))
h = int(input("ВВеди верх: "))
number = random.randrange(l,h)
print("Случайное чилсо:", number)
