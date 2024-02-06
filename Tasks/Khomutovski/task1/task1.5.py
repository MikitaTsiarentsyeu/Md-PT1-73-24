from random import randint


a, b = map(int, input("Enter first and second value separated by a space : ").split())
print(f"You random number is:  {randint(a, b)}")
