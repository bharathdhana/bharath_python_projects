def calculate_sum(numbers):
    
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
   
    if not numbers:
        return 0
    total_sum = calculate_sum(numbers)
    return total_sum / len(numbers)


numbers = [1, 2, 3, 4, 5]
print("Sum:", calculate_sum(numbers))       
print("Average:", calculate_average(numbers))  



















"""
#Getter and Setter:
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #Setter
    def name(self):
        return self._name
    #Getter
    def name(self,name):
        self.name=name

    #Setter
    def age(self):
        return self._age
    #Getter
    def age(self,age):
        if age>=0:
            self.age =age
        else:
            raise ValueError("Age cannot be negative")

    def __repr__(self):
        return f"Student(name={self.name},age={self.age})"

student = Student("Maran",20)
print(student.name)
print(student.age)

try:
    student.age=-5
except ValueError as e:
    print(e)
"""
