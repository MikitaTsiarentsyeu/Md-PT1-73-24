def power(number, number_power): 
    if (number_power == 0):
        return 1
    return number * power(number, number_power - 1)

print(power(2, 10))    