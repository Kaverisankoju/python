from abc import ABC ,abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def get_role(self):
        pass
class Student(Person):
    def __init__(self,student_id,name,age):
        super().__init__(name,age)
        self.student_id=student_id
        self.enrolled_course=[]
        
    def get_role(self):
        return 'role is:Student'
    def get_enrolled_course(self):
        print("enrolled courses are:",self.enrolled_course)
    def add_course(self,course_name):
        self.enrolled_course.append(course_name)
    def student_info(self):
        print("student id:",self.student_id)
        print("student name:",self.name)
        print("student age:",self.age)
class Teacher(Person):
    def __init__(self,teacher_id,name,age):
        super().__init__(name,age)
        self.teacher_id=teacher_id
        self.assigned_courses=[]
    def teacher_info(self):
        print("teacher id:",self.teacher_id)
        print("teacher name:",self.name)
        print("teacher age:",self.age)
    def get_role(self):
        return 'role is:Teacher'
    def get_assigned_courses(self):
        print("assigned corces are:",self.assigned_courses)
    def add_assigned_course(self,assigned_course):
        self.assigned_courses.append(assigned_course)
class Course:
    def __init__(self,course_name,course_code):
        self.course_name=course_name 
        self.course_code=course_code
        self.teacher=None
        self.enrolled_students=[] 
    def set_teacher(self,teacher):
        self.teacher=teacher
    def get_enrolled_students(self,student):
        self.enrolled_students.append(student)
    def show_details(self):
        print("course name :",self.course_name) 
        print("course code:",self.course_code) 
        print("teacher:",self.teacher) 
        print("enrolled students:",self.enrolled_students)  
class Department:
    def __init__(self,department_name):
        self.department_name=department_name
        self.courses=[]
        self.teachers=[]
        self.students=[]
    def get_courses(self):
        print("course list:",self.courses)
    def add_courses(self,course):
        if course in self.courses:
              print('course already in courses list')
        else:
              self.courses.append(course)
    def get_teachers(self):
        print("teachers list:",self.teachers)
    def add_teachers(self,teacher):
        self.teachers.append(teacher)
    def get_students(self):
        print("students list:",self.students)
    def add_students(self,student):
        self.students.append(student)
    def summary_info(self):
        print("courses :",self.courses)
        print("teachers :",self.teachers)
        print("students :",self.students)
class Dept:
    def __init__(self,departments):
        self.departments=departments
        self.departments=[]
    def get_dept(self):
        print("departments:",self.departments)
    def add_dept(self,department):
        self.departments.append(department)
    def dept_info(self):
        print("dept info:",self.departments)
        
stu1=Student(3,'kavya',20)
stu1.student_info()
stu1.add_course('python')
stu1.add_course('java')
stu1.get_enrolled_course()
stu1.enrolled_course
print(stu1.get_role())
t1=Teacher(5,'ravi',35)
t1.teacher_info()
t1.add_assigned_course('Full stack')
t1.add_assigned_course('DS')
t1.get_assigned_courses()
t1.assigned_courses
print(t1.get_role())
c1=Course('Data Structures', '(CS101)')
c1=Course('Algorithms', '(CS102)')
c1.get_enrolled_students('janu')
c1.get_enrolled_students('jahnavi')
c1.set_teacher('Keerthi')
c1.enrolled_students
c1.course_name
c1.course_code
c1.show_details()
d1=Department('Computer Science')
d1.add_courses('OS')
d1.add_courses('OS')
d1.add_courses('DBMS')
d1.add_teachers('mamatha')
d1.add_teachers('kavya')
d1.add_students('manju')
d1.add_students('anjali')
d1.courses
d1.teachers
d1.students
d1.get_courses()
d1.get_students()
d1.get_teachers()
d1.summary_info()
d2=Dept(1)
d2=Dept(2)
d2=Dept(2)
d2.add_dept(33)
d2.add_dept(44)
d2.dept_info()
