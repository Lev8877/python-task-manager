python_students = {"Лев", "Анна", "Иван", "Мария"}
sql_students = {"Иван", "Мария", "Алексей", "Олег"}

print(*(set(python_students) | set(sql_students)))
print("Python и SQL: ", *(set(python_students) & set(sql_students)))
print("Python: ", *(set(python_students) - set(sql_students)))
print("Python или SQL: ", *(set(python_students) - set(sql_students)),*(set(sql_students) - set(python_students)))
print("Множеста равные?: ",set(python_students) == set(sql_students))
print("Есть ли общие элементы?: ",len((set(python_students) & set(sql_students))) > 0)
python_students.add("Кирилл")
sql_students.add("Кирилл")
sql_students.remove("Алексей")
sql_students.discard("Олег")
print(python_students)
print(sql_students)