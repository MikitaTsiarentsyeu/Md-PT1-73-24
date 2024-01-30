inp = input("Enter the line eq in the format y=kx+b:\n")

inp = inp.lower().replace(' ', '')

if "=x" in inp:
    inp = inp.replace("=x", "=1x")

inp = inp.replace('y=', '')

# print(inp[2], inp[-1])

res = inp.split('x')
k = float(res[0])
b = float(res[1])
print(f"k={k}; b={b}")

x = float(input("Enter the x value:\nx="))

y = k*x+b
print(f"y={y}")