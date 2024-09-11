"""
class Area():
    def __init__(self):
        pass
    def calculate_area(self,length,breadth):
       
        return f"Area of Rectangle:{length* breadth}"

Obj = Area()
print(Obj.calculate_area(10,15))
"""

#Using Keys and arguments:
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alisson", age=24, city="Melbourne")
