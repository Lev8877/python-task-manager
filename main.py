tasks = []
for _ in range(int(input("Введите количество задач которые вы хотите записать: "))):
    title = input("Введите название задачи: ")
    description = input("Введите описание: ")
    priority = int(input("Введите приоритет от 1 до 5: "))
    hours = float(input("Введите время выполнения в часах: "))
    completion = int(input("Введите процент выполнения: "))
    status = None


    if not title.strip() or not(1 <= priority<= 5) or hours < 0 or not(0 <=completion<= 100):
        print("Некорректные данные задачи")   
    else:
        if completion == 0:
            status = "Задача не начата"
        elif completion == 100:
            status = "Задача завершена"
        else:
            status = "Задача в процессе"
        
        task = {
            "title": title,
            "description": description,
            "priority": priority,
            "hours": hours,
            "completion": completion,
            "is_important": priority >= 4,
            "is_long": hours > 3,
            "is_completed": completion == 100,
            "is_urgent": (
                priority == 5 or (priority >= 4 and hours <= 2)
            ) and completion != 100,
            "status": status

        }
        tasks.append(task)
        print("Задача добавлена")
if tasks:
    for task in tasks:
        print(task)
        if task["is_urgent"]:
            print("Внимание задание срочное!")
        if task["is_long"] and task["priority"] <= 2:
            print("Задачу можно запланировать на потом")