import json 

students = [
    {"name": "Лев", "grade": 5},
    {"name": "Анна", "grade": 4},
    {"name": "Иван", "grade": 3},
]

with open(r"C:\Users\kiri-\OneDrive\Desktop\Мой проект на github\python-task-manager\python-exercises\day_08\students.json", "w", encoding="utf-8") as file:
    json.dump(students,file,ensure_ascii=False,indent=4)


with open(r"C:\Users\kiri-\OneDrive\Desktop\Мой проект на github\python-task-manager\python-exercises\day_08\students.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    for student in data:
        print(f"{student['name']} - {student['grade']}")
