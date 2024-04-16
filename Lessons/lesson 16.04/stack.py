class StackWithIteration:

    def __init__(self, *items):
        self.__items = []
        self.__len = 0
        if items:
            self.__items.extend(items)
            self.__len = len(items)

    def push(self, item):
        self.__items.insert(0, item)
        self.__len+=1

    def pop(self):
        self.__len-=1
        return self.__items.pop(0)
    
    def __str__(self):
        return f"{StackWithIteration.__name__}({','.join(str(x) for x in self.__items)})"
    
    def __len__(self):
        return self.__len
    
    def __iter__(self):
        self.__iteration_index = 0
        return self
    
    def __next__(self):
        if self.__iteration_index >= self.__len:
            del self.__iteration_index
            raise StopIteration
        item = self.__items[self.__iteration_index]
        self.__iteration_index += 1
        return item
    
    def __getitem__(self, key):
        try:
            return self.__items[key]
        except IndexError:
            raise IndexError(f"{StackWithIteration.__name__} index out of range")

    def __setitem__(self, key, value):
        try:
            self.__items[key] = value
        except IndexError:
            self.__items.append(value)

st = StackWithIteration(1,2,3,4,5)
print(st)

st.pop()
print(st)

st.push(10)
print(st)

st.push("test")
print(st)

# st.push(st)
# print(st)

st.push(range(10))
print(st)

print(len(st))

for i in st:
    print(i)

print(st[1])

st[0] = 0
print(st)

st[100] = 100
print(st)