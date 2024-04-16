import random

class Animal:

    def say_something(self):
        print(self.__class__.__name__)

class Dog:

    def say_something(self):
        print("woof")

class Cat:
    
    def say_something(self):
        print("meow")

class Human:
    
    def say_something(self):
        print("hm")

# a = Animal()
# a.say_something()

# d = Dog()
# d.say_something()

def test_call(a):
    a.say_something()

animals = [Animal(), Dog(), Cat(), Human(), "test"]
random.shuffle(animals)

# for a in animals:
#     print(dir(a))
#     test_call(a)

print(hasattr(animals[0], "say_something"))

d = Dog()
d.test = "value"
d.__setattr__("test", "value")

print(d.__getattribute__("jhgjh"))

