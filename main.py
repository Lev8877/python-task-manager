task = input("Введите название задачи: ")
description = input("Введите описание: ")
priority = int(input("Введите приоритет от 1 до 5: "))
hours = float(input("Введите время выполнения в часах: "))
completion = int(input("Введите процент выполнения: "))

if task == "" or not(1 <= priority<= 5) or hours < 0 or not(0 <=completion<= 100):
    print("Некорректные данные задачи")   
else:
    print(f"Задача создана \nНазвание: {task}\nОписание: {description}\nПриоритет: {priority}\nВремя выполнения: {hours:.2f} ч.\nВыполнено: {completion}% \nВажная задача: {priority == 4 or priority == 5}\nДолгая задача: {hours > 3} \nЗавершена: {completion == 100}")
    if (priority == 5 or (priority >= 4 and hours <= 2)) and completion != 100:
        print("Внимание задача срочная!")
    if completion == 0:
        print("Задача не начата")
    elif completion == 100:
        print("Задача завершена")
    else:
        print("Задача в процессе")
    if hours > 3 and priority <= 2:
        print("Задачу можно запланировать на потом")