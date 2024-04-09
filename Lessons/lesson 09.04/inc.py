class Dog:

    __breeds = ["wss", "shepherd", "setter", "pointer"]

    def __init__(self, name, breed, color, age):
        self.set_name(name)
        self.__set_breed(breed)
        self.__set_color(color)
        self.__set_age(age)

          
    def set_name(self, name):
        self.__name = name.lower()

    def get_name(self):
        return self.__name.capitalize()
    
    def __set_breed(self, breed):
        if breed in Dog.__breeds:
            self.__breed = breed
        else:
            self.__breed = Dog.__breeds[-1]

    def get_breed(self):
        return self.__breed
    
    def set_color(self, color):
        if self.__breed == "wss":
            color = "white"
        self.__color = color

    def get_color(self):
        return self.__color

    def get_age(self):
        return f"{self.__age} years"
    
    def __set_age(self, age):
        if age < 0 or age > 25:
            age = 0
        self.__age = age

    name = property(get_name, set_name)
    __dog_breed = property(get_breed, __set_breed)
    breed = property(get_breed)
    color = property(get_color, set_color)
    age = property(get_age)

    def get_older(self):
        self.__age += 1

    def bark(self):
        print("WOOF!")

    def __print_age(self):
        print(self.__age)

# d = Dog()
# d.name = "zefirka"
# d.breed = "wss"
# d.color = "white"

d = Dog("zefirka", "wss", "color", 3)

print(d.get_name())

# print(d.__age)
# d._Dog__print_age() name mangling
print(d._Dog__age)

# print(Dog.name, d.name)

print(Dog.__dict__)
print(d.__dict__)
# print(Dog().__dict__)

print(d.get_age())
d.get_older()
print(d.get_age())

# d.set_name("new name")
# print(d.get_name())
d.name = "new name"
print(d.name)

# d.breed = "test"
print(d.breed)