students = [
    {"name": "Лев", "grade": 5, "age": 18},
    {"name": "Анна", "grade": 3, "age": 17},
    {"name": "Иван", "grade": 4, "age": 20},
]

def get_adult_students(students):
    result = []
    for student in students:
        if student["age"] >= 18:
            result.append(student["name"])
    print(f"Эти студенты старше или равны 18-ти лет: {result}")

def get_students_with_min_grade(students, minimum_grade = 3):
    result = []
    for student in students:
        if student["grade"] == minimum_grade:
            result.append(student["name"])
    print(f"У этих студентов минимальная проходная оценка: {result}")     

def calculate_average_grade(students):
    if not students:
        return
    s = 0 
    for student in students:
        s += student["grade"]
    print(f"Среднее арф. студентов: {s/len(students)}")

get_adult_students(students)
get_students_with_min_grade(students, minimum_grade = 3)
calculate_average_grade(students)