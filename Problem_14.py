#Constructor and Destructor Calling:
class Cons_dest:
    def __init__(self):
        print("Hello everyone,Constructor is called")

    def __del__(self):
        print("Thank You,Destructor is called")


new = Cons_dest()
del new

    



"""
class Student:
    student_count=0
    
    def __init__(self,name):
        self.name = name
        Student.student_count+=1
        print(f"Student's name:{self.name}")

def print_studentname():
    print(f"Number of student displayed: {Student.student_count}")


student1 = Student("Arun")
student2 = Student("Catherine")
student3 = Student("Dhanavan")
print_studentname()

"""
