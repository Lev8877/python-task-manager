def create_student(name, age, grade=0):
    return {
        "name": name,
        "age": age,
        "grade": grade,
        "is_adult": age >= 18
    }


def print_student(student):
    print(f"Имя студента: {student['name']}")
    print(f"Возраст студента: {student['age']}")
    print(f"Оценка студента: {student['grade']}")
    print(f"Он совершеннолетний: {student['is_adult']}")


student = create_student("Лев", 18, 4)
print_student(student)