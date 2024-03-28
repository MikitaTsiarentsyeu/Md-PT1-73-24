'1. Write a recursive function to reverse a string.'
def rever(str_1, i=-1, rev=[]):
    if len(rev) == len(str_1):
        rev = ''.join(rev)
        return rev
    rev.append(str_1[i])
      
    return rever(str_1, i-1, rev)
str_1 = 'level'

print(rever(str_1))

'2. Write a recursive function to check whether a given string is a palindrome.'
def palindrome(str_pol):
    str_pol = str_pol.lower()
    if len(str_pol) == 1:
        return True
    else:
        if str_pol[0] == str_pol[-1]:
            return palindrome(str_pol[1:-1])
        else:
            return False

str_pol = 'rever'
print(palindrome(str_pol))

def palindrome_v2(str_1):
    f = rever(str_1)
    if str_1 == f:
        return True
    else:
        return False
print(palindrome_v2(str_1))

'3. Write a recursive function to count the number of occurrences of a given character in a string.'
def count_numb(str_n, symb, i=0, n=0):
    if i == len(str_n):
        return n
    if str_n[i] == symb:
        n += 1
    return count_numb(str_n, symb, i+1, n)
str_n = 'occurrences'
print(count_numb(str_n, 'c'))

'4. Write a recursive function to calculate the power of a given number.'
def power_numb(numb, power):
    if power == 0:
        return 1
    return numb * power_numb(numb, power-1)

print(power_numb(2, 4))

'5. Write a recursive function to find the Nth number in the Fibonacci sequence.'
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))





 