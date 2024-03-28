import io

# with open("test.txt", 'w') as f:
#     f.write("test")

try:
    is_open = False
    f = open("test.txt", 'w')
    is_open = True
    f.read()
    f.write("test")
except FileNotFoundError:
    is_open = False
    print("file not found")
except io.UnsupportedOperation:
    print("operation is not supported")
else:
    print("else!")
finally:
    if is_open:
        f.close()
