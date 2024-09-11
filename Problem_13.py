class Rectangle:
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length = length

    def calc_area(self):
        return f"Area of Rectangle is:{self.length*self.breadth}"

    def perimeter(self):
        return f"Perimeter of Rectangle is :{2* (self.length+self.breadth)}"

rect = Rectangle(12,24)
print(rect.calc_area())
print(rect.perimeter())



"""
class Person:
    def __init__(self):
        pass
    def display(self,name,age):
        return f"The Person's Name is {name}, he is {age} years old."

person=Person()
print(person.display("Charlie",24))
        
"""
