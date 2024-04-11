
class Food:

    def __init__(self, name, food_type) -> None:
        self.name = name
        self.food_type = food_type


class Animal:

    def __init__(self, name):
        self.name = name
        

    def eat(self, something):
        print(f"{self.name} eating {something.name}")

    def phe(self):
        print("phe...")


class Carnivore(Animal):

    def eat(self, something):
        if something.food_type == "meat":
            Animal.eat(self, something)
        else:
            super().phe()

class Herbovore(Animal):

    def eat(self, something):
        if something.food_type == "herbal":
            # super().eat(something)
            Animal.eat(self, something)
        else:
            super().phe()


class Omnivore(Herbovore, Carnivore): pass


grass = Food("grass", "herbal")
stake = Food("stake", "meat")

tiger = Carnivore("Tigger")
rabbit = Herbovore("Rabbit")

tiger.eat(stake)
tiger.eat(grass)

rabbit.eat(stake)
rabbit.eat(grass)

dog = Omnivore("Zefirka")

dog.eat(stake)
dog.eat(grass)

print(Omnivore.__mro__)