from decimal import Decimal as D
from fractions import Fraction as F
import math

# num = 15
# print(type(num))

# print(12+3, 12-3, 12*3, 12/3)
# print(type(12+3), type(12-3), type(12*3), type(12//3))

# print(type(12.0*3))

# x = 15.5
# x = int(x)
# print(x)
# x = float(x)
# print(x)

# print(round(3.5))
# print(round(4.4), round(4.5), round(4.6))
# print(round(5.5))
# print(round(6.5))
# print(round(7.5))
# print(round(8.5))

# print(0.1+0.1+0.1==0.3)
# print(0.1+0.1+0.1)

x = D('0.1')
print(type(x), x)
print(x+x+x)

x = F('0.1')
print(type(x), x)
print(x+x+x)

# x = 144
# print(x**0.5)
# print(math.sqrt(x))