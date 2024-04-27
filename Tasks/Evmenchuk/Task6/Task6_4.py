num = int(input('Enter a number: \n'))
exp = int(input('Enter his degree: \n'))


def power(num, exp):
    if (exp == 1):
        return (num)
    if (exp != 1):
        return (num * power(num, exp - 1))


print('The result of exponentiation is:', power(num, exp))
