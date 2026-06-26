from utils import is_task_urgent, get_status

from utils import read_command

def create_task():
    title = input("Введите название задачи: ")
    description = input("Введите описание: ")
    priority = read_command("Введите приоритет от 1 до 5: ") 
    hours = read_command("Введите время выполнения в часах: ")
    completion = read_command("Введите процент выполнения: ")

    if (
        not title.strip()
        or not 1 <= priority <= 5
        or hours < 0
        or not 0 <= completion <= 100
    ):
        print("Некорректные данные задачи")
        return 

    status = get_status(completion)

    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "hours": hours,
        "completion": completion,
        "is_important": priority >= 4,
        "is_long": hours > 3,
        "is_completed": completion == 100,
        "is_urgent": is_task_urgent(priority,hours,completion),
        "status": status
    }


    if task["is_urgent"]:
        print("Внимание: задача срочная!")

    if task["is_long"] and task["priority"] <= 2:
        print("Задачу можно запланировать на потом")
    
    return task 
    
def show_tasks(tasks):
    if not tasks:
        print("Список пуст")
        return 
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
    return 

def get_all_stats(tasks):
    if not tasks:
        print("Список задач пуст")
        return
    
    for index, task in enumerate(tasks, start=1):
        print(
            f"Процент выполнения {index} задачи: "
            f"{task['completion']}% - {task['status']}"
        )

def show_urgent_tasks(tasks):
    if not tasks:
        print("Список задач пуст")
        return

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
    return 

def update_task_completion(tasks):
    if not tasks:
        print("Список задач пуст")
        return

    print("\nЗадачи:")

    for index, task in enumerate(tasks, start=1):
        print(
            f"{index}. {task['title']} — "
            f"{task['completion']}%, {task['status']}"
        )

    task_number = read_command("\nВведите номер задачи для изменения: ") 

    while not 1 <= task_number <= len(tasks):
        task_number = read_command("Введите существующий номер задачи: ")

    task_index = task_number - 1

    new_completion = read_command("Введите новый процент выполнения: ")

    while not 0 <= new_completion <= 100:
        new_completion = read_command("Введите процент от 0 до 100: ")

    tasks[task_index]["completion"] = new_completion
    tasks[task_index]["is_completed"] = new_completion == 100

    task = tasks[task_index]

    task["is_urgent"] = is_task_urgent(
        task["priority"],
        task["hours"],
        new_completion
)

    task["status"] = get_status(new_completion)

    print("Процент выполнения успешно изменён")
    print(f"Новый статус: {tasks[task_index]['status']}")

    if tasks[task_index]["is_urgent"]:
        print("Внимание: задача срочная!")
    return

def delete_task(tasks): 
    if not tasks:
        print("Список задач пуст")
        return 

    print("\nЗадачи:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']}")

    task_number = read_command("\nВведите номер задачи для удаления: ")

    while not 1 <= task_number <= len(tasks):
        task_number = read_command("Введите существующий номер задачи: ")
    task_index = task_number - 1
    removed_task = tasks.pop(task_index)

    print(f"Задача «{removed_task['title']}» удалена")

