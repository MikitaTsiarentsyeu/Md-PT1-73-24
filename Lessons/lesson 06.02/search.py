s = "hj%$&^gdcjhgdfhj.,./,/kgdj hd"

d = {}
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
print(d)

s = "London, is, the, capital of the Great Britain"
s = s.split()
print(s)
