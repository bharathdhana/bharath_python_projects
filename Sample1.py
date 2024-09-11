class A:
    def show(self):
        return "A"
            
class B(A):
    def show(self):
        return "B"
    
a=A()
b=B()
print(a.show(),b.show())


class A:
    def too(self):
        return 1

class B(A):
    def too(self):
        return 2

class C(B):
    pass

c=C()
print(c.too())

class A:
    def __init__(self):
        self.var1 = 1

class B:
    def __init__(self):
        self.var2=2

obj=B()
print()

class X:
    def __init__(self, x):
        self.x = x

class Y(X):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

obj = Y(1, 2)
print(obj.x, obj.y)

"""
class Parent:
    def __init__(self,value):
        self.value =value

class Child(Parent):
    def __init__(self,value):
        super().__init__(value)
        self.value*=2

obj.Child(5)
print(obj.value)
"""

class Demo:
    def __init__(self):
        self.x=1
    def change(self):
        self.x=10

class Demo_derived(Demo):
    def change(self):
        self.x=self.x+1
        return self.x
    
def main():
    obj = Demo_derived()
    print(obj.change())

main()

"""
class Sales:
    def __init__(self):
        id=100

val = Sales(123)
print(val.id)
"""

class A:
    def __init(self):
        self.multiply(15)
        print(self.i)

    def multiply(self,i):
        self.i=4*i

class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self,i):
       self.i= 2*i

obj=B()
