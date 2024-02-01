#Generate random number inside user inputed range and print it
import random

min_range = input("Input minimum range of RNG number:")
max_range = input("Input maximum range of RNG number:")

rng_number = random.randint(int(min_range), int(max_range))
print(f"Your random number is inside range: {min_range} <= RND <= {max_range} and is:{rng_number}")