students = [
    {"name": "Лев", "grade": 5},
    {"name": "Анна", "grade": 4},
    {"name": "Иван", "grade": 3},
    {"name": "Мария", "grade": 5},
    {"name": "Олег", "grade": 2}
]

summ = 0 
maximum = students[0]["grade"]
max_name = students[0]["name"]
count_grade5 = 0 
good_students = [] 

for student in students:
    print(student["name"],student["grade"])
    summ += student["grade"]
    if maximum < student["grade"]:
        maximum = student["grade"]
        max_name = student["name"]
    if student["grade"] == 5:
        count_grade5 += 1
    if student["grade"] >= 4:
        good_students.append(student["name"])

print(summ/len(students))
print(max_name)
print(count_grade5)
print(good_students)
