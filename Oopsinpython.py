#Oops Concepts --- Classes and Objects
"""
class demo():
    pass #placeholder
a=10
print(a)
print(type(demo))

class car():
    pass
swift=car()
print(isinstance(swift,car))  #To check that if the object is in instance or subclass of class or tuple of classes
print(isinstance(a,int))
print(type(swift))
print(type(car))

#class attributes
class Student():
    name = "Ram Kumar"
    age = 25
obj = Student()
print(getattr(obj,'name'))
print(getattr(obj,'age'))
#print(getattr(obj,'gender'))
print(Student.name)     #Dot Notation
print(Student.age)

#set attributes
setattr(Student,'name','Simson')
print(Student.name)
setattr(Student,'age',28)
print(Student.age)

#add attributes using dot notation
Student.city="Salem"
print(Student.city)

#Dictionary fr classes
print(Student.__dict__)

#deleting using attribute as delattr
delattr(Student,"city")
print(Student.__dict__)

#deleting using dot notation
del Student.age
print(Student.__dict__)
"""

#Instance attributes
"""
class user:
    course = "java"
a=user()
print(user.__dict__)
print(user.course)
print(a.__dict__)
print(a.course)
a.course="C++"
print(a.course)
a1=user()
print(a1.course)
"""

#Methods in classes
"""
class Student:
    name = "Bharath"
    age = 24
def printall():
    print("Name:",Student.name)
    print("Age:",Student.age)
    print(Student.__dict__)
    value = getattr(Student,"name")
    print(value)
    #print(Student.__dict__['printall']())
    

printall()
"""

#Instance Methods
"""
class Student:
    name = "Bharath"
    age = 24
    def printall(self,gender):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",gender)

instance=Student()
instance.printall("Male")
    
#Constructors
#--init-- methods in python
class user:
    def __init__(self):
        print("Call when new instance created")

obj=user()

class user:
    def __init__(self,name):
        print("Instance created")
        self.name=name
    def printall(self):
        print("Name:",self.name)

obj=user("Bharath")
obj.printall()
print(obj.__dict__)
"""
#Property Decorator
"""
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @property
    def msg(self):
        return f"{self.name} is {self.age} years old"
        #self.msg=self.name + "is" + str(self.age) + "years old"

obj=user("Bharath",24)
print(obj.name)
print(obj.age)
print(obj.msg)
#print(obj.msg)
obj.age=25
print(obj.age)
print(obj.msg)
"""

#Property Decorators using getters and setters:
"""
class Student:
    def __init__(self,total):
        self._total=total

    
    def average(self):
        return self._total/5.0
    
    @property  #getter
    def total(self):
        return self._total

    @total.setter  #setter
    def total(self,t):
        if t<0 or t>500:
            raise ValueError("Invalid Total")
            #print("Invalid Total")
            #else:
        self._total=t

obj=Student(450)
print("Total:",obj.total)
print("Average:",obj.average())

try:
    obj.total=600
except ValueError as e:
    print(e)
"""

#Methods in Property Decorators
"""
class Student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0

    def getter(self):
        return self._total

    def setter(self,t):
        if t<0 or t>500:
            print("Invalid Error")
        else:
            self._total=t
            
    total=property(getter,setter)
    
obj=Student(450)
print("Total:",obj.total)
print("Average:",obj.average())

"""

#Class Method Decorator:
"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printDetail(self):
        return f"Name: {self.name} Age: {self.age}"

obj=Student("Sam",22)
print(obj.printDetail())


class Student:
    count=0
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.count+=1

    def printDetail(self):
        return f"Name: {self.name} Age: {self.age}"

    @classmethod
    def total(cls):
        return cls.count

obj=Student("sam",24)
print(obj.printDetail())
obj=Student("sam",24)
print(obj.printDetail())


print("total admission:",Student.total())
"""

#Static Methods:
"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printDetail(self):
        return f"Name:{self.name} Age:{self.age}"

    @staticmethod
    def welcome():
        print("Static method in python")


obj=Student("Ram",28)
print(obj.printDetail())
obj.welcome()

"""

#Abstraction and Encapsulation:
"""
class Library:
    def __init__(self, books):
        self.books = books
        self.borrowed_books = []

    def list_books(self):
        print("Available books:")
        for book in self.books:
            print("-", book)

    def borrow_books(self, borrow_book):
        if borrow_book in self.books:
            self.books.remove(borrow_book)
            self.borrowed_books.append(borrow_book)
            print(f"{borrow_book} has been borrowed successfully.")
        else:
            print(f"Sorry, {borrow_book} is not available.")

    def receive_books(self, receive_book):
        if receive_book in self.borrowed_books:
            self.borrowed_books.remove(receive_book)
            self.books.append(receive_book)
            print(f"{receive_book} has been returned successfully.")
        else:
            print(f"Invalid book: {receive_book}")

books = ['C', 'C++', 'Java']
obj = Library(books)

msg = """
        #1. Display books
        #2. Borrow book
        #3. Return book
"""

while True:
    print(msg)
    ch = input("Enter your choice: ")
    if ch == '1':
        obj.list_books()
    elif ch == '2':
        book = input("Enter book name to borrow: ")
        obj.borrow_books(book)
    elif ch == '3':
        book = input("Enter book name to return: ")
        obj.receive_books(book)
    else:
        print("Thank you, visit again!")
        break
"""        

#Inheritance
#Single Inheritance
"""
class Nokia:
    company="Nokia India"
    website="www.nokia_india.com"

    def contact_details(self):
        print(f"Address: Cherry road, new bus stand,Salem")

class Nokia1100(Nokia):
    def __init__(self):
        self.name="Nokia 1100"
        self.year=1998

    def product_details(self):
        print(f"Name: {self.name}")
        print(f"Year: {self.year}")
        print(f"Company: {self.company}")
        print(f"Website: {self.website}")

Mobile=Nokia1100()
print(Mobile.product_details())
print(Mobile.contact_details())
"""


#Multiple inheritance
"""
class Father:
    def Driving(self):
        print("Driving Vehicles")
    def Chess(self):
        print("Playing chess with dad")
        
class Mother:
    def Cooking(self):
        print("Cooking Food")
    def Chess(self):
        print("Playing Chess with mom")

class Son(Mother,Father):
    def travel(self):
        print("Loves Travelling")

new_Son = Son()
new_Son.Driving()
new_Son.Chess()
new_Son.Cooking()
new_Son.Chess()
new_Son.travel()
"""

#Multilevel Inheritance:
"""
class Grandfather:
    def Ownhouse(self):
        print("Grandpa's House")

class Father(Grandfather):
    def Property(self):
        print("Father's Property")

class Son(Father):
    def OwnBike(self):
        print("Son's Bike")

Mul_Son = Son()
Mul_Son.Ownhouse()
Mul_Son.Property()
Mul_Son.OwnBike()
    
"""

#Function Overriding:
"""
class Employee:
    def Workinghrs(self):
        self.hrs = 50
    def Printhrs(self):
        print("Total Working Hours:",self.hrs)
    def resethrs(self):
        self.Workinghrs()
class Trainee(Employee):
    def Workinghrs(self):
        self.hrs = 60
    def Printhrs(self):
        print("Total Working Hours:",self.hrs)
    def resethrs(self):
        self.Workinghrs()

emp = Employee()
emp.Workinghrs()
emp.Printhrs()

tra = Trainee()
tra.Workinghrs()
tra.Printhrs()

#RESET
emp.resethrs()
emp.Printhrs()

tra.resethrs()
tra.Printhrs()
"""

#Handling Diamond Problems:
"""
class A:
    def display(self):
        print("Display A")

class B(A):
    def display(self):
        print("Display B")

class C(A):
    def display(self):
        print("Display C")

class D(B,C):
    def display(self):
        print("Display D")

Obj = D()
Obj.display()
"""

#Operator Overloading:
"""
a=10
b=20
print(a+b)

a="Sim"
b="Sons"
print(a+b)


class Addition:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        if isinstance(other,Addition):
            return Addition(self.a+other.a)
        return NotImplemented

    def __repr__(self):
        return f"Addition({self.a})"
    
class Subtraction:
    def __init__(self,a):
        self.a=a

    def __sub__(self,other):
        if isinstance(other,Subtraction):
            return Subtraction(self.a-other.a)
        return NotImplemented
    
    def __repr__(self):
        return f"Subtraction({self.a})"

    
val1=Addition(10)
val2=Addition(22)

result = val1+val2
print("Total:",result.a)

val1=Subtraction(10)
val2=Subtraction(22)

result = val1-val2
print("difference:",result.a)
"""

#abstract classes
"""
from abc import ABC,abstractmethod

class Bank(ABC):
    
    def loan(self):
        pass
    def credit(self):
        pass
    def debit(self):
        pass

class ICICI(Bank):
    def loan(self):
        print("Provide 7% Interest Loan")
    def credit(self):
        print("ICICI provide credit")
    def debit(self):
        print("ICICI provide debit")
    def Card(self):
        print("ICICI provide Card")


Obj = ICICI()
Obj.loan()
Obj.credit()
Obj.debit()
Obj.Card()

"""

#File handling:
"""
file =open("C:/Users/Bharath/Downloads/Sample.txt","r")
print(file.read())
"""


"""
try:
    file =open("C:/Users/Bharath/Downloads/Samle.txt","r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found")
else:
    file.close()
"""
#Readlines
"""
try:
    file =open("C:/Users/Bharath/Downloads/Sample.txt","r")
    print(file.readline())
    print(file.readlines())
except FileNotFoundError:
    print("Error: File not found")
else:
    file.close()
"""
"""
try:
    file =open("C:/Users/Bharath/Downloads/Sample.txt","r")
    print(file.readlines())
except FileNotFoundError:
    print("Error: File not found")
else:
    file.close()
"""

#Line by Line
"""
try:
    file =open("C:/Users/Bharath/Downloads/Sample.txt","r")
    for line in file:
        print(line)
except FileNotFoundError:
    print("Error: File not found")
else:
    file.close()
"""
#Writing in file:
"""
file = open("C:/Users/Bharath/Downloads/Sample.txt","w")
file.write("Universe Always falls in love with the Stubborn Heart.")
file.close()
file =open("C:/Users/Bharath/Downloads/Sample.txt","r")
print(file.readlines())
"""
#Appending in file:
"""
file = open("C:/Users/Bharath/Downloads/Sample.txt","a")
file.write("Learn Pyschology and Phylosophy")
file.close()
file =open("C:/Users/Bharath/Downloads/Sample.txt","r")
print(file.readlines())
"""
#Deleting file:
"""
import os

file_path = "C:/Users/Bharath/Downloads/New Text Document.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print("File has been deleted")
else:
    print("File not found")

##os.rmdir("folder_name")

"""
