l = [5,12,3,3,1,2]

print(sorted(l), l)

# l[0], l[-1] = l[-1], l[0]
# print(l)

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]

print(l)

# l = [33, 1, 2, 3, 3, 5, 12]

# for j in range(len(l)-1):
#     for i in range(len(l)-1):
#         if l[i] > l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]

#     print(l)

for j in range(len(l)-1):
    min_i = j
    for i in range(j, len(l)):
        if l[i] < l[min_i]:
            min_i = i
    l[j], l[min_i] = l[min_i], l[j]
    print(l)
