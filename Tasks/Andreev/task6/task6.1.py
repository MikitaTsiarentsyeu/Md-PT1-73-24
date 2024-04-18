def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


original_string = "hello world"
reversed_string = reverse_string(original_string)
print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")