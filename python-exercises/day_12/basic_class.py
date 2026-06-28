class Student:
    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade 


student1 = Student("Анна", 5)
student2 = Student("Иван", 3)

print(student1.name, student1.grade)
print(student2.name, student2.grade)