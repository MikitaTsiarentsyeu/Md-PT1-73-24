c = "cat"
d = "dog"
p = "parrot"

"a cat, a dog and a parrot"

res = "a " + c + ", a " + d + " and a " + p
print(res)
"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a "
"a cat, a dog and a parrot"

print("a {}, a {} and a {}".format(c, d, p))
print("a {}, a {} and a {}".format(p, d, c))
print("a {2}, a {1} and a {0}".format(c, d, p))
print("a {cat}, a {dog} and a {parrot}".format(cat=c, dog=d, parrot=p))

print(f"a {c}, a {d} and a {p}")