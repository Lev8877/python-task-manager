try:
    with open(r"C:\Users\kiri-\OneDrive\Desktop\Мой проект на github\python-task-manager\python-exercises\day_08\notes.txt","r",encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден")
else:
    print("Файл успешно прочитан")
finally:
    print("Работа с файлом завершена")
