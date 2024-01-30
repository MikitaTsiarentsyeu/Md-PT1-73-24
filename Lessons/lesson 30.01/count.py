text = "London is the capital of Great Britain"

d = {}
for symbol in text:
    d[symbol] = d.get(symbol, 0) + 1

print(d)