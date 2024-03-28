# 5. Write a recursive function to find the Nth number in the Fibonacci sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# n = 6 => 5

def FibbonachiRecur(deapth, numberA = 0, numberB = 1):
    global seekingNumber
    if deapth <= 0:
        return seekingNumber
    
    seekingNumber = numberA + numberB
    FibbonachiRecur(deapth - 1, numberB, seekingNumber)

seekingNumber = 0
userDeapth = (int) (input("Enter your index: "))
FibbonachiRecur(userDeapth - 2)

print(f"Your fibbonachi number: {seekingNumber}")