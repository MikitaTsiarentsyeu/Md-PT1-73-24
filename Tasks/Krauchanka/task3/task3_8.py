# 8. Write a program that takes a list of numbers as 
# input and returns the average of all numbers in the list.

number= input("Enter your numbers separated by space: ").split ()
number= [float(i) for i in number]
sum = 0
count =0
for i in number:
    sum += (i)
    count +=1

average_value= sum/count

print(f"sum=", {sum}, "count=",{count}, "average value: ",{average_value})

