def Palindrome(s, i):
    if(i > len(s)/2):
       return True
    ans = False
    if((s[i] is s[len(s) - i - 1]) and Palindrome(s, i + 1)):
      ans = True
    return ans
 
str = input("Input string: ")
if (Palindrome(str, 0)):
    print("Yes")
else:
    print("No")