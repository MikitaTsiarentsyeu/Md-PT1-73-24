class Engine:

    def __init__(self, power, size):
        self.__power = power
        self.__size = size

    def get_power(self):
        return self.__power
    
    def get_size(self):
        return self.__size
    
    power = property(get_power)
    size = property(get_size)

e = Engine(100, 1.8)
print(e.power, e.size)
# e.power = 111 error

class SerialCar:

    __colors = ["red", "blue", "black"]

    def __init__(self, make, model, color, engine):
        self.__make = make
        self.__model = model
        self.set_color(color)
        self.engine = engine

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model

    def set_color(self, color):
        if color not in SerialCar.__colors:
            color = SerialCar.__colors[-1]
        self.__color = color

    def get_color(self):
        return self.__color
    

sc = SerialCar("vw", "golf", "black", e)
print(sc.engine.power)

sc.engine = Engine(200, 3.6)
print(sc.engine.power)


class SuperCar:

    class __CarEngine(Engine):

        # def __init__(self, power, size):
        #     self.__power = power
        #     self.__size = size

        # def get_power(self):
        #     return self.__power
        
        # def get_size(self):
        #     return self.__size
        
        # power = property(get_power)
        # size = property(get_size)

        pass

    __colors = ["red", "blue", "black"]

    def __init__(self, make, model, color, power, size):
        self.__make = make
        self.__model = model
        self.set_color(color)
        self.__engine = SuperCar.__Engine(power, size)

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model

    def set_color(self, color):
        if color not in SuperCar.__colors:
            color = SuperCar.__colors[-1]
        self.__color = color

    def get_color(self):
        return self.__color
    
    # def get_engine(self):
    #     return self.__engine
    
    # engine = property(get_engine)

    def get_engine_power(self):
        return self.__engine.power
    
    def get_engine_size(self):
        return self.__engine.size
    
    engine_size = property(get_engine_size)
    engine_power = property(get_engine_power)

super_car = SuperCar("ferrari", "la ferrari", "red", 300, 8.0)
print(super_car.engine_power)