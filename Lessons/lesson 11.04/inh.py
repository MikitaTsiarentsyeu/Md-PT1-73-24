class Animal:

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("I'm sleeping")

class NotSleepingAnimal(Animal):

    def sleep(self):
        print("I'm not sleeping, I'm waiting")

class Cat(Animal):

    pass

c = Cat("Whiskers")
c.sleep()
print(c.name)

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def hunt(self):
        print("I'm hunting")

d = Dog("Good boy", "shepherd")
d.hunt()
d.sleep()
print(d.name)


class FlyingAnimal(Animal):

    def move(self):
        print("I'm flying")

class RunningAnimal(Animal):

    def move(self):
        print("I'm running")

class SwimmingAnimal(Animal):

    # def move(self):
    #     print("I'm swimming")

    pass


class Duck(SwimmingAnimal, RunningAnimal, FlyingAnimal):

    def fly(self):
        # FlyingAnimal.move(self)
        super().move()

    def run(self):
        # RunningAnimal.move(self)
        super().move()

    def swim(self):
        # SwimmingAnimal.move(self)
        super().move()

d = Duck("Donald")
d.fly()
d.run()
d.swim()
# d.move()

# print(isinstance(d, object))
# print(isinstance(Duck, object))

# d.sleep()
# print(d.__dict__)
# print(Duck.__dict__)
# print(SwimmingAnimal.__dict__)
# print(Animal.__dict__)

print(Animal.__mro__)
print(SwimmingAnimal.__mro__)
print(Duck.__mro__)


