# Keyword Arguments
def my_function(a, b, c):
    """Prints"""
    print(a)
    print(b)
    print(c)


my_function(1, 2, 3)  # 1 2 3
my_function(b=3, c=1, a=2)  # 2 3 1


def default_function(a=1, b=2, c=3):
    """Prints with default values"""
    print(a)
    print(b)
    print(c)


default_function()  # 1 2 3
default_function(b=4)  # 1 4 3
default_function(4, 9)  # 4 9 3
default_function(20)  # 20 2 3


# Unlimited positional arguments
def add(*args):  # The asterisk is the magic, the variable could be anything
    """Adds with args"""
    for n in args:  # All args will be stored in a tuple
        print(n)


add(3)  # 3
add(2, 3, 4, 5)  # 14


# **kwargs: Many Keyworded Arguments
def calculate(n, **kwargs):  # asterisk is the magic again.
    """Kwargs"""
    # All kwargs are stored in a dict
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# Class with kwargs
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car)

my_other_car = Car(make="Nissan")
print(my_other_car)  # will error out if we didn't have the get()
