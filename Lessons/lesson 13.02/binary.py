with open("test.txt", 'w') as f:
    f.write("some text content")

with open("test.txt", 'rb') as f:
    print(repr(f.read()))



chunk = 10000
with open("test.pptx", 'rb') as donor:
    with open("test_copy.pptx", 'wb') as recepient:
        file_part = donor.read(chunk)
        while file_part:
            recepient.write(file_part)
            file_part = donor.read(chunk)
    print("done!")