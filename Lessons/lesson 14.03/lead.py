# import csv
# csv.reader(open("test.txt", 'w'))

# import module as mdl

# module = "test"

# print(mdl, type(mdl))

# print(mdl.test)

# from module import test as tst, test_lst, test_func

# print(tst, test_lst, test_func)

# test_lst.append("new elem")
# test_func()

# from module import *

# print(test, test_lst, test_func)

import module

print(module.test)

print(module.__name__)

import test

print(test.__name__)

print(__name__)