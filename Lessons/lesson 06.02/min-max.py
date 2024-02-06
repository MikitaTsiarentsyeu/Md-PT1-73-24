l = [2,4,4,3,2,1,3,45,6,99,7,5,42]

# s_l = sorted(l)
# min, max = s_l[0], s_l[-1]
# print(min, max)

min = l[0]
max = l[0]
for i in l:
    if i < min:
        min = i
    if i > max:
        max = i
print(min, max)

target = 13
target_i = False
count = 0
for i, e in enumerate(l):
    if e == target:
        target_i = i
        count += 1
print(target_i, count)