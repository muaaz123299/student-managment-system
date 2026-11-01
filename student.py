class Student:
    def __init__(self,student_id,name,age,grades):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.grades=grades
    def student_id (self):
        print("student_id :",self.student_id,"name:",self.name,"age:",self.age,"grades:",self.grades,)


s1=Student(1,"nomi",20,[90,80,70])
s2=Student(2,"muaaz",18,[99,98,99])
    