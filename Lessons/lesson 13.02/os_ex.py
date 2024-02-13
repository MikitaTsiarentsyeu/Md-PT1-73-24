import os


# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())

# f = open("lesson 13.02\\test.txt", 'r')
# print(f)

levels = ["level 1", "level 2", "level 3"]
path = os.sep.join(levels)
path = os.path.join("level 1", "level 2", "level 3")
print(path)

old_cwd = os.getcwd()

# os.makedirs(path)
# os.chdir(path)
# print(os.getcwd())
# open("test_file.txt", 'w')

for item in os.walk(old_cwd):
    print(item)

# os.chdir(path)
# os.remove("test_file.txt")
# os.chdir(old_cwd)
# os.removedirs(path)