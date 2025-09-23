# class Marks:
#     def __init__(self,so_marks,math_marks):
#         self.so_marks=so_marks
#         self.math_marks=math_marks
#     def __add__(self,other):
#         print(self.so_marks+ other.so_marks)
#         print(self.math_marks+other.math_marks)
#     def display(self):
#         print(self.so_marks)
# m1=Marks(2,3)
# m2=Marks(6,5)
# m3=Marks('k','a')
# m4=Marks('v','e')
# m5=Marks(95,90) #display first argument
# m1+m2
# m3+m4
# m5.display()

class Vechicle:
    def __init__(self,color,price):
        self.color=color
        self.price=price
    def display(self):
        print("Car color is",self.color)
        print("price of car is",self.price)
    def drive(self):
        print("vechicle in drive mode")
class Bike(Vechicle):
    #method overriding
    def drive(self):
        super().drive()
        print("bike in drive mode")
    #method overloading
class Addition:
    def add(self,*a):
        return sum(a)
    #operator overloading
class Marks:
    def __init__(self,python_marks,HTML_marks):
        self.python_marks=python_marks
        self.HTML_marks=HTML_marks
    def __add__(self,other):
        print("Addition is",self.python_marks+self.HTML_marks)
        print("Addition is",other.python_marks+other.HTML_marks)  
    def __sub__(self,other):
        print("substraction is",self.python_marks-self.HTML_marks)
        print("substraction is",other.python_marks-other.HTML_marks) 
    def __mul__(self,other):
        print("multiplication is",self.python_marks*self.HTML_marks)
        print("multiplication is",other.python_marks*other.HTML_marks) 
    def __truediv__(self,other):
        print("division is ",self.python_marks/self.HTML_marks)
        print("division is ",other.python_marks/other.HTML_marks)         
m1=Marks(90,90)   
m2=Marks(95,85)
m1+m2
m1-m2
m1*m2
m1/m2
v1=Vechicle('black',50000)
b1=Bike('red',30000)
a1=Addition()
print(a1.add(2,3))
print(a1.add(2,3,4,5,6))
print(a1.add(9))
print(a1.add())
b1.drive()
v1.display()
b1.display()