s=input("u_text: ")
newstr = s
l = ["a", "e", "i", "o", "u", "A", "E", "I", "U", "O"]
for i in s:
    if i in l:
        newstr = newstr.replace(i, "")
        
print(newstr)