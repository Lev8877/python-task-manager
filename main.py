tasks = []

while True:
    print("\nМеню\n")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Показать срочные задачи")
    print("4. Изменить процент выполнения")
    print("5. Удалить задачу")
    print("0. Выход")

    command = input("\nВведите номер команды: ")

    if command == "1":
        title = input("Введите название задачи: ")
        description = input("Введите описание: ")
        priority = int(input("Введите приоритет от 1 до 5: "))
        hours = float(input("Введите время выполнения в часах: "))
        completion = int(input("Введите процент выполнения: "))

        if (
            not title.strip()
            or not 1 <= priority <= 5
            or hours < 0
            or not 0 <= completion <= 100
        ):
            print("Некорректные данные задачи")
            continue

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
                priority == 5
                or (priority >= 4 and hours <= 2)
            ) and completion != 100,
            "status": status
        }

        tasks.append(task)
        print("Задача успешно добавлена")

        if task["is_urgent"]:
            print("Внимание: задача срочная!")

        if task["is_long"] and task["priority"] <= 2:
            print("Задачу можно запланировать на потом")

    elif command == "2":
        if not tasks:
            print("Список задач пуст")
            continue

        print("\nВсе задачи:")

        for index, task in enumerate(tasks, start=1):
            print(
                f"\n{index}. {task['title']}\n"
                f"   Описание: {task['description']}\n"
                f"   Приоритет: {task['priority']}\n"
                f"   Время выполнения: {task['hours']:.2f} ч.\n"
                f"   Выполнено: {task['completion']}%\n"
                f"   Статус: {task['status']}\n"
                f"   Важная: {task['is_important']}\n"
                f"   Долгая: {task['is_long']}\n"
                f"   Срочная: {task['is_urgent']}"
            )

    elif command == "3":
        if not tasks:
            print("Список задач пуст")
            continue

        urgent_found = False

        print("\nСрочные задачи:")

        for index, task in enumerate(tasks, start=1):
            if not task["is_urgent"]:
                continue

            print(
                f"\n{index}. {task['title']}\n"
                f"   Приоритет: {task['priority']}\n"
                f"   Время выполнения: {task['hours']:.2f} ч.\n"
                f"   Выполнено: {task['completion']}%\n"
                f"   Статус: {task['status']}"
            )

            urgent_found = True

        if not urgent_found:
            print("Срочных задач нет")

    elif command == "4":
        if not tasks:
            print("Список задач пуст")
            continue

        print("\nЗадачи:")

        for index, task in enumerate(tasks, start=1):
            print(
                f"{index}. {task['title']} — "
                f"{task['completion']}%, {task['status']}"
            )

        task_number = int(
            input("\nВведите номер задачи для изменения: ")
        )

        while not 1 <= task_number <= len(tasks):
            task_number = int(
                input("Введите существующий номер задачи: ")
            )

        task_index = task_number - 1

        new_completion = int(
            input("Введите новый процент выполнения: ")
        )

        while not 0 <= new_completion <= 100:
            new_completion = int(
                input("Введите процент от 0 до 100: ")
            )

        tasks[task_index]["completion"] = new_completion
        tasks[task_index]["is_completed"] = new_completion == 100

        tasks[task_index]["is_urgent"] = (
            tasks[task_index]["priority"] == 5
            or (
                tasks[task_index]["priority"] >= 4
                and tasks[task_index]["hours"] <= 2
            )
        ) and new_completion != 100

        if new_completion == 0:
            tasks[task_index]["status"] = "Задача не начата"
        elif new_completion == 100:
            tasks[task_index]["status"] = "Задача завершена"
        else:
            tasks[task_index]["status"] = "Задача в процессе"

        print("Процент выполнения успешно изменён")
        print(f"Новый статус: {tasks[task_index]['status']}")

        if tasks[task_index]["is_urgent"]:
            print("Внимание: задача срочная!")

    elif command == "5":
        if not tasks:
            print("Список задач пуст")
            continue

        print("\nЗадачи:")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']}")

        task_number = int(
            input("\nВведите номер задачи для удаления: ")
        )

        while not 1 <= task_number <= len(tasks):
            task_number = int(
                input("Введите существующий номер задачи: ")
            )

        task_index = task_number - 1
        removed_task = tasks.pop(task_index)

        print(f"Задача «{removed_task['title']}» удалена")

    elif command == "0":
        print("Программа завершена")
        break

    else:
        print("Неизвестная команда")

