

class Dog:

    name = ""
    breed = ""

    def bark(self):
        print("BARK!")


class HuntingDog(Dog): 

    target = ""

    def hunt(self):
        print(f"hunting {self.target}")

d = HuntingDog()
d.name = "Hunter"
d.breed = "hunter"
d.bark()

d.target = "mice"
d.hunt()