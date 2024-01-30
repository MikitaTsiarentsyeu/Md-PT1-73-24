d = {}
print(d, type(d), len(d))

d = {"one":1, "two":2, "three":[3, 3.0]}
print(d, type(d), len(d))

print(d["three"])
# print(d["test"])

d[4] = "four"
print(d)

d[4] = "four four four four"
print(d)

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

print("test" in d)

print(d.get("test"))
print(d.get("test", "-1"))
print(d)