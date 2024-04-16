
class Train:

    def __init__(self, n):
        self.__cart_count = n

    def __len__(self):
        return self.__cart_count
    
    def __str__(self):
        return f"train with {self.__cart_count} carts"
    
    def __eq__(self, value):
        # if not isinstance(value, Train):
        #     return False
        try:
            return len(self) == len(value)
        except:
            return False
    
    def __add__(self, other):
        try:
            return Train(len(self)+len(other))
        except:
            raise TypeError(f"cannot add objects of type {type(other).__name__} to objects of type {self.__class__.__name__}")

t = Train(5)
print(len(t))

print(t)

short = Train(6)
long = Train(18)
print(short == long, short == Train(6), short == 6)

print(Train(5)+Train(10))