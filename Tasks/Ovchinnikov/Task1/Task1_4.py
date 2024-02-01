#Convert money from USD to BYN
usd_to_byn_multiplier = 2.5

usd_amount = input("Enter money amount in USD:")
byn_amount = float(usd_amount) * usd_to_byn_multiplier
print(f"Byn amount after conversion:{byn_amount}")