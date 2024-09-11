#Classes and Subclasses
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    def __repr__(self):
        return f"Rectangle (length={self.length},breadth={self.breadth})"

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2*math.pi*self.radius
        
        
    def __repr__(self):
        return f"Circle (radius:{self.radius})"

rectangle = Rectangle(5,8)
circle = Circle(5)

print(rectangle)
print(f"Area:{rectangle.area()},Perimeter:{rectangle.perimeter()}")

print(circle)
print(f"Area:{circle.area()},Perimeter:{circle.perimeter()}")
        


"""
#inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return f"Person(name:{self.name},age:{self.age})"

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def __repr__(self):
        return f"Student(name={self.name},age={self.age},student_id={self.student_id})"


person = Person("Anna",28)
student = Student("Danny",25,586614)

print(person)
print(student)
 """       
    
        
