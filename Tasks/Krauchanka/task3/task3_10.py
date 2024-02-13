# 10. Write a program that takes a list of numbers as input 
# and returns the largest prime number in the list.


number= list( input("Enter your numbers separated by space: ").split ())
number= [int(num) for num in number]
max_prime=[]

for num in number:
    if num>1:
        for x in range(2, int(num ** 0.5) + 1): 
            if num % x == 0:
                break
        else:
            max_prime.append(num)
print(max_prime)

if len(max_prime):    
    print(f"max value", {max(max_prime)})   
else:          
    print("prime number not found")
        


