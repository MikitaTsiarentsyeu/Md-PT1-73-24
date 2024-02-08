# f = open("test.txt", 'w')
# print(f, type(f))

# f.write("test")

# f.close()

with open("test.txt", 'w') as f:
    f.write("new test\n")
    f.write("some text\n")
    f.write("another test\n")
    f.writelines(["line 1\n", "line 2\n", "line 3\n"])

with open("test.txt", 'r') as f:
    content = f.readlines()
    print(content)

with open("test_txt_file.txt", 'r') as f:
    content = f.readlines()

content = [line.replace(',', '.').capitalize() for line in content]

with open("test_txt_file.txt", 'w') as f:
    content = f.writelines(content)


with open("test.txt", 'r') as f:
    chunk = 1
    while chunk:
        chunk = f.read(10)
        print(repr(chunk))

with open("test.txt", 'r') as f:
    for line in f:
        print(repr(line))


with open("test.txt", 'r') as f:
    chunk = 1
    while chunk:
        chunk = f.read(10)
        # f.seek(0)
        print(repr(chunk))

with open("test.txt", 'a') as f:
    f.write("appended content\n")

with open("test.txt", 'a+') as f:
    f.write("appended content from a+")
    f.seek(0)
    f.write("overwrite?\n")
    print(repr(f.read()))

with open("test.txt", 'r+') as f:
    print(repr(f.read()))
    f.seek(0)
    print(f.readlines())
    f.write("new content from r+")

with open("test.txt", 'r+') as f:
    f.write("overwrite!")
    for i in range(10):
        f.write(' ')

with open("test.txt", 'w+') as f:
    print(repr(f.read()))
    f.write("it's a new file")
    f.seek(0)
    print(repr(f.read()))
    f.seek(0)
    f.write("test")