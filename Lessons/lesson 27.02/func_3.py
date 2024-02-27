from functools import reduce

l = [1,2,3,4,5,6,7,8,9]
map_obj = map(print, l)
print(list(map_obj))
# print(list(range(10)))

map_obj = map(lambda x: ord(x), map(lambda x: chr(x*100), l))
print(list(map_obj))

filter_obj = map(lambda x: chr(x), filter(lambda x: x%3==0, map(lambda x: x*10, l)))
print(list(filter_obj))

l = [1,2,3,4,5]
print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: f"{x}-{y}", l))

print(reduce(lambda x, y: x if x < y else y, l))