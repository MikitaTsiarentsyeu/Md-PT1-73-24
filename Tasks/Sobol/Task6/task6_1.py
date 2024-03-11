def recursion(string):
    if string == "":
        return string
    else:
        return recursion(string[1:]) + string[0]

print(recursion(input("Input string: ")))