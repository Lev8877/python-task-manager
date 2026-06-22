task = input("Введите название задачи: ")
description = input("Введите описание: ")
priority = int(input("Введите приоритет от 1 до 5: "))
hours = float(input("Введите время выполнения в часах: "))
complition = int(input("Введите процент выполнения: "))

if task == "" or not(1 <= priority<= 5) or hours < 0 or not(0 <=complition<= 100):
    print("Некорректные данные задачи")   
else:
    print(f"Задача создана \nНазвание: {task}\nОписание: {description}\nПриоритет: {priority}\nВремя выполнения: {hours:.2f} ч.\nВыполненено: {complition}% \nВажная задача: {priority == 4 or priority == 5}\nДолгая задача: {hours > 3} \nЗавершена: {complition == 100}")