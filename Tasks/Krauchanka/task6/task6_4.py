# 4. Write a recursive function to calculate the power of a given number.

def power(x, degree):
    if degree == 1:
        return x
    elif degree == 0:
        return 1
    else:
        return x * power(x, degree - 1)

print(power(6, 4)) 
print(power(7, 0)) 
print(power(9, 1))