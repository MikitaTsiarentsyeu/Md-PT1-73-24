# user text = Write a program that takes a string as input from a user and returns the number of vowels
a = input()
l = ["a", "e", "i", "o", "u", "A", "E", "I", "U", "O"]
count=0
for i in a:
    if i in l:
       count+=1
print(count)