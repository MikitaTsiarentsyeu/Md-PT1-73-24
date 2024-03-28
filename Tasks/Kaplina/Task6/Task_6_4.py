# 4. Write a recursive function to calculate the power of a given number.

# Var #1
def calc_power(i=0, res=1, num=2, power=10):
    if power == 0:
        return 1
    if i != power:
        res *= num
        return calc_power(i + 1, res, num, power)
    else:
        return res

print(calc_power())
        
# Var #2
def calc_power(num, power):
    if power == 0:
        return 1
    elif power == 1:
        return num
    else:
        return num * calc_power(num, power - 1)

print(calc_power(2, 10))


