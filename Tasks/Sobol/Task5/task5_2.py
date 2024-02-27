def reversed_list(lst):
    result = ""
    for i in range(len(lst)):
        result = lst[i] + result
    return result
print(reversed_list(input("Input string: ")))    