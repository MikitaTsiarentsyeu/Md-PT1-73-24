# {
#     "name": "Zephyrka",
#     "age": 4,
#     "breed": "wss"
# }

# {
#     "name": "Max",
#     "age": 5,
#     "breed": "shepherd"
# }

# ('name', 'age', 'breed')

class Dog:
    "test doc string"

    name = "Zephyrka"
    age = 3
    breed = "wss"
    # test = "test"

    def bark(self):
        print(f"Woof! My name is {self.name}")

print(Dog.name)
# Dog.bark()

Dog.age = 4
print(Dog.age)

zephirka = Dog()
print(zephirka, type(zephirka))
print(Dog, type(Dog))


print(zephirka.age, Dog.age)
zephirka.age = 5
print(zephirka.age, Dog.age)
Dog.age = 10
print(zephirka.age, Dog.age)

# print(zephirka.name, Dog.name)
# Dog.name = "Max"
# print(zephirka.name, Dog.name)

max = Dog()
print(zephirka.name, max.name, Dog.name)
max.name = "Max"
print(zephirka.name, max.name, Dog.name)
Dog.name = "Good boy"
print(zephirka.name, max.name, Dog.name)

print(Dog.__dict__)
print(max.__dict__)
print(zephirka.__dict__)
print(Dog().__dict__)

print(max.age)
print(max.__getattribute__("age"))
print(max.__getattribute__("name"))
# print(max.__getattribute__("test"))
# max.test

# max.age = 7
max.__setattr__("age", 7)
print(max.age)
max.test = "test"
print(max.__dict__)
print(Dog.__dict__)

Dog.new_attr = "new attr value"
print(Dog.__dict__)
print(max.new_attr)

print(id(max))
max.bark()