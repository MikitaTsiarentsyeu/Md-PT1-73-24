def power(base, exponent):
   
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        
        return 1 / (base * power(base, -exponent - 1))


основание = int(input("Введи число: "))
показатель = int(input("Введи стпень: "))
результат = power(основание, показатель)
print(f"{основание}^{показатель} = {результат:.2f}")
