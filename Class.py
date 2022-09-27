#Creating The Class
from unicodedata import name


class student:
    totalstudent=0
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def Display(self):
        print("Name:",self.name,"\nDepartment:",self.department)

#Creating Object Of The Class
stu1=student("rahul","BCA")
stu2=student("Mihir","BSC")

#Access The Class Member
stu1.Display()
stu2.Display()

#Built in  Function
print(getattr(stu1,"name"))
print(hasattr(stu2,"sem"))
setattr(stu1,"sem","5")
print("After Set Sem In the Stu1: ",getattr(stu1,"sem"))
delattr(stu1,"sem")
print("After Delete Sem In the Stu1: ",stu1.Display())

#Built In Class Atribute
print("__dict__: ",stu1.__dict__)
print("__doc__: ",stu1.__doc__)
print("__module__ : ",stu1.__module__)

#Delete The Object
del stu1

class department(student):
    def __init__(self, name, department):
        super().__init__(name, department)

c1=department("rahul","BCA")
c1.Display()

#Operator Overloading
class Vector:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __str__(self):
       return 'Vector (%d, %d)' % (self.a, self.b)
   def __add__(self,other):
       return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)


        

