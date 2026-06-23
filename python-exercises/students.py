students = [
    {"name": "Лев", "age": 20, "grade": 5},
    {"name": "Анна", "age": 19, "grade": 4},
    {"name": "Иван", "age": 21, "grade": 3}
]
max_val = []
print(students[0]["name"])
print(students[1]["grade"])
students[2]["grade"] = 4
students.append({"name": "Чара", "age": 20, "grade":5})
print(len(students))
names = []
for student in students:
    max_val.append(student["grade"])
    names.append(student["name"])
print(names)
s = 0
max_val = max(max_val)
for student in students:
    s += student["grade"]
print(s/len(students))
best_students = []
for student in students:
    if student["grade"] == max_val:
        best_students.append(student["name"])
print("Лучшие студенты: ",*best_students)