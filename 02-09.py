#OOPS=>
#varibles,methods=>
#types of variables=>
#types of methods=>
class Student:
    college='Engineering College'
    def __init__(self,id,name,branch):
        self.id=id
        self.name=name
        self.branch=branch
        
        
    def display(self):
        print("student id is",self.id)
        print("student name",self.name)
        print("student branch",self.branch)
        print("college name is",Student.college)
    @classmethod
    def change_college(cls,new_college):
        cls.college=new_college
        print("\n ---after changing the name of college---")
        print(f"college name changed to",{cls.college})
    @staticmethod
    def is_eligible(branch):
        if branch=='CSE':
            return True
        else:
            return False
        
s1=Student(1,'Ravi','CSE')
s2=Student(2,'Rani','EEE')
s3=Student(3,'Karthik','ECE')
print("\n-------student1 details------")
s1.display()
print("\n-------student2 details------")
s2.display()
print("\n-------student3 details------")
s3.display()

Student.change_college("University College")
print("\n ---after change name of college student1 details---")
s1.display()  
print("\n---branch eligibility check---")
print("Is Ravi eligible (CSE)?", Student.is_eligible("CSE"))
print("Is Rani eligible (EEE)?", Student.is_eligible("EEE"))