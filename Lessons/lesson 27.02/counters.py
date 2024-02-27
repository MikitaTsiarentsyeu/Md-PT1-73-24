
# def counter(start=0):
#     return start+1

# count = False
# count = {}

def counter(start=0):
    count = start
    def inner():

        nonlocal count
        count += 1

        # global count
        # if count != False:
        #     count = count + 1
        # else:
        #     count = start + 1

        # if start in count:
        #     count[start] += 1
        # else:
        #     count[start] = start+1

        return count
    return inner

def counter(start=0):
    def inner():
        nonlocal start
        start += 1
        return start
    return inner

from_10 = counter(10)
print(from_10())
print(from_10())
print(from_10())
print(from_10())

from_100 = counter(100)
print(from_100())
print(from_100())
print(from_100())
print(from_100())

from_10_new = counter(10)
print(from_10_new())
print(from_10_new())
print(from_10_new())
print(from_10_new())

print(id(from_10))
print(id(from_100))
print(id(from_10_new))

