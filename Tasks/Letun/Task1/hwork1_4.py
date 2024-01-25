#4.Write a program that converts some amount of money from USD to BYN, ask a user for the amount, store the ratio inside the program itself.

usd_to_byn = 3.167  # Соотношение доллара США к белорусскому рублю

usd_amount = float(input("Введите сумму в долларах США: "))

byn_amount = usd_amount * usd_to_byn

print(f"{usd_amount} долларов США равны {byn_amount} белорусским рублям.")


