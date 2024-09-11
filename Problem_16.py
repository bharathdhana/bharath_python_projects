#Printing Length:
def print_length(value):
    try:
        length = len(value)
        print(f"The length of {value} is {length}")
    except TypeError:
        print(f"Length is not Applicable for the type")


print_length("hello")
print_length({1,2,3,4,5})
print_length((10,20,30,40,50,60))
print_length([11,22,33,44,55,66,77,88])
print_length({'a':1,'b':2})
print_length(56)
print_length(25.46) 



















"""
class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bow Bow !!"

class Cat(Animal):
    def sound(self):
        return "Meow Meow !!"


def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
"""
