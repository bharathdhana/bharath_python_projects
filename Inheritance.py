# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving"

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

    def bark(self):
        return f"{self.name}, the {self.breed}, says Woof!"

# Create an instance of Dog
dog = Dog("Buddy", "Golden Retriever")

# Call methods from base and derived classes
print(dog.move())    
print(dog.bark())     
