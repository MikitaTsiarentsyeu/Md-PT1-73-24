from decimal import Decimal as D

USD_money_value = input("Enter the USD: ")
course = D('3.1498') # 22 january 2024
BYN_money_value = D(USD_money_value) * course
print("BYN: ", BYN_money_value)