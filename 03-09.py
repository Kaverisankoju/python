#DECORATORS=>
#which adds some extra functionality to existing function
def my_decorator(func):
    def wrapper():
        print('before calling the function...')
        func()
        print('after calling the function...')
    return wrapper
@my_decorator
def say_hello():
    print('Hello! world')
say_hello()

#Class method Decorators=>
#A class method is a method that works with the class itself, not just objects.
#It takes cls (class) as the first parameter instead of self (object).
class Student:
    school_name='ZPHS'
    def __init__(self,name):
        self.name=name
    @classmethod
    def get_school(cls):
        return cls.school_name
print('by using direct class name')
print('school name is',Student.school_name)
print('by using class method..')
print('school name is',Student.get_school())

#static method=>
#A static method is like a normal function but placed inside a class for better org
class MathOperations:
    @staticmethod
    def add(a,b):
        return 'addition is:',a+b
    def sub(a,b):
        return 'substraction is:',a-b
    def mul(a,b):
        return 'multiplication is:',a*b
    def div(a,b):
        if b!=0:
            return 'division is:',a/b
        else:
            return 'division is not possible'
print(MathOperations.add(6,3))
print(MathOperations.sub(6,3))
print(MathOperations.mul(6,3))
print(MathOperations.div(6,3))