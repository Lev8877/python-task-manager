with open(r"C:\Users\kiri-\OneDrive\Desktop\Мой проект на github\python-task-manager\python-exercises\day_08\notes.txt", "w", encoding="utf-8") as file: 
    file.write("Изучить файлы\n")
    file.write("Изучить JSON\n")
    file.write("Добавить сохранение задач\n")
with open(r"C:\Users\kiri-\OneDrive\Desktop\Мой проект на github\python-task-manager\python-exercises\day_08\notes.txt", "a", encoding="utf-8") as file: 
    file.write("Сделать Git-коммит\n")
with open(r"C:\Users\kiri-\OneDrive\Desktop\Мой проект на github\python-task-manager\python-exercises\day_08\notes.txt", "r", encoding="utf-8") as file: 
    for line in file:
        print(line.strip())
