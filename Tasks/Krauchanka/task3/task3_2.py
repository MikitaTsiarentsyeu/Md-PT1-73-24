
# 2. Write a program that takes a list of numbers as input and
# returns the sum of all even numbers in the list.

number= input("Enter your numbers separated by space: ").split ()
number= [int(i) for i in number]

sum = 0
l=[]
for a in number:
        if a %2==0:
            sum+= (a)
            l.append(a)    
    
print (number)       
print (l, "sum of all even numbers ",sum)  

