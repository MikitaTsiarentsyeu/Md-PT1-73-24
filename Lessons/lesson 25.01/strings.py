test = "some text to be used in this program"
test2 = 'some text to be used in this program'

print(type(test))
print(test == test2)
print(repr(test))
print(repr(test2))

"some 'long' text"
'some "long" text'

test3 = '''some text to be used in this program'''
test4 = """some text to be used in this program"""
print(test == test2 == test3 == test4)

text = """line 1
line 2
line 3"""

# """This code is working fine,
#     but kinda slow"""

print(text)

text = 'I\'m \too old for this\n stuff'
print(text)

print(chr(50), chr(500), chr(5000), chr(50000))
print(ord('T'), ord('&'), ord('썐'))

folder = "C:\Drive D\Projects\IT Academy\Python\Md-PT1-73-24\repo\Md-PT1-73-24\Lessons\lesson 25.01"
folder = r"C:\Drive\n\n\n\n\n\\\\\\\\\\ D\Projects\IT Academy\Python\Md-PT1-73-24\repo\Md-PT1-73-24\Lessons\lesson 25.01"
print(folder)

print(len("test"))
print(len("\n"))
print(len(r"\n"))

empty_str = ""
print(empty_str, type(empty_str), len(empty_str), bool(empty_str))

print(str(4.0))
print(str(str))

s = "my very long string"
print(len(s))
print(s[0], s[1], s[2], s[3], s[4])
print(s[-1], s[-2], s[-3], s[-4])
print(s[len(s)-1])
print(s[-len(s)])

print(s[0:7])
print(s[0:len(s)])
print(s[:])

print(s[3:-3])
print(s[3:-3:2])
print(s[::3])
print(s[::-1])

print(s.upper(), id(s))
s = s.lower()
print(s, id(s))
print(s.upper().casefold())

print("TeSt" == "test")
print("TeSt".lower() == "test".lower())
print(ord('T'), ord('t'))
print(ord('\n'))


print('s' in s, '!' in s)
print('test' in s, 'my' in s)

print(s.count(' '), s.count('!'))
print(s[s.find(' ')], s[s.find('very')], s[s.find('!')])

test = "new test"
e = 't'
# test[test.find('e')].upper()
e.upper()
e_i = test.find(e)
new_str = test[:e_i] + e.upper() + test[e_i+1:]
print(new_str)

print("0"*8)

print(test.replace(e, e.upper()), test)
print(s.replace('!', '@'))

s = s.replace('!', '@').replace("very", "not so").replace(' ', '_').upper()
print(s)

sku = "2024_SPRST_BLK"
print(sku.split('_'))
parts = sku.split('_')
print('/'.join(parts))

test = "   a b c d e     "
print(repr(test.strip()))
test = "!!!!!!a b c d e!!!!"
print(repr(test.strip('!')))


