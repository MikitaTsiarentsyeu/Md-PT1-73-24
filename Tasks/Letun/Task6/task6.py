# 1. Write a recursive function to reverse a string.

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)


# 2. Write a recursive function to check whether a given string is a palindrome.

def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

test_string1 = "radar"
test_string2 = "Hello, World!"
print(f"Is '{test_string1}' a palindrome? {is_palindrome(test_string1)}")
print(f"Is '{test_string2}' a palindrome? {is_palindrome(test_string2)}")


# 3. Write a recursive function to count the number of occurrences of a given character in a string.

def count_char_in_string(char, string):
    
    if len(string) == 0:
        return 0
    
    if string[0] == char:
        return 1 + count_char_in_string(char, string[1:])
    else:
        return count_char_in_string(char, string[1:])

s = "Hello, World!"
c = "o"
result = count_char_in_string(c, s)
print(f"Символ '{c}' встречается в строке '{s}' {result} раз(а).")


# 4. Write a recursive function to calculate the power of a given number.

def power(base, exponent):

  if exponent == 0:
    return 1
  else:
    return base * power(base, exponent - 1)

base = 2
exponent = 5
result = power(base, exponent)
print("Result:", result)


# 5. Write a recursive function to find the Nth number in the Fibonacci sequence.

#    0, 1, 1, 2, 3, 5, 8, 13, 21

#    n = 6 => 5

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    n = int(input("Enter the position of the Fibonacci number you want to find: "))
    print(f"The {n}th Fibonacci number is {fibonacci(n)}")


if __name__ == "__main__":
    main()
