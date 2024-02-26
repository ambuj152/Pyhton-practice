class Student:
    
         Student_college="Kashi institute of technology"

         def __init__(self, fullname, marks,age):
            self.fullname=fullname
            self.marks=marks
            self.age=age
         def avg_marks(self):
               sum=0
               for val in self.marks:
                     sum=sum+val
               print("hi",self.fullname,"your average marks is",sum/3)
               

s1=Student("Ambuj",[97,56,60],24)
print("good morning",s1.fullname)
s1.avg_marks()
print("your age is",s1.age)


    