def recursive_power(n:int, power:int):
    if power == 1:
        return n
    return n * recursive_power(n, power-1) 
    

    
n = int(input('Enter a number:\n'))
p = int(input('To what power should we raise the number?:\n'))
    
print(f'{n} in power {p} is {recursive_power(n, p)}')