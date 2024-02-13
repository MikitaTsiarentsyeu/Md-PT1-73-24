"4. Write a program that takes a list of numbers as input and returns the second largest number in the list."

string = input('Enter the list in the format 1 21 35 4 : \n')
n = list(string.split(' '))

"Option 1"
first = 0
second = 0
for i in range(len(n)):
    if int(n[i]) > first and int(n[i])> second:
        second = first
        first = int(n[i])
    elif int(n[i]) < first and int(n[i]) > second:
        second = int(n[i])
print(second)

"Option 2"
# max = n[0]

# for j in n:
#     if j > max:
#         max = j
# t = n.remove(max)
# max = n[0]          
# for i in n:
#     if i > max:
#         max = i
# print(max)
        
"Option 3"
# for j in range(len(n)-1):
#     m = j
#     for i in range(j, len(n)):
#         if int(n[i]) > int(n[m]):
#             m = i
#     n[j], n[m] = n[m], n[j]
# print(n[1]) 