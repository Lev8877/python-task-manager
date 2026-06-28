class Student:
    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade 

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Оценка: {self.grade}")
    
    def is_successful(self):
        return self.grade >= 4


student1 = Student("Анна", 5)
student2 = Student("Иван", 3)
student1.show_info()
student2.show_info()
print(student1.is_successful())
print(student2.is_successful())