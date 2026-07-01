from utils import read_command
from task_model import Task

def create_task():
    title = input("Введите название задачи: ")
    description = input("Введите описание: ")
    priority = read_command("Введите приоритет от 1 до 5: ") 
    hours = read_command("Введите время выполнения в часах: ")
    completion = read_command("Введите процент выполнения: ")
    deadline_input = input("Введите дату дедлайна: ").strip()
    deadline = deadline_input or None

    if (
        not title.strip()
        or not 1 <= priority <= 5
        or hours < 0
        or not 0 <= completion <= 100
    ):
        print("Некорректные данные задачи")
        return 

    # status = Task.get_status()

    task = Task(title,description,priority,hours,completion,deadline)

    # task = {
    #     "title": title,
    #     "description": description,
    #     "priority": priority,
    #     "hours": hours,
    #     "completion": completion,
    #     "is_important": priority >= 4,
    #     "is_long": hours > 3,
    #     "is_completed": completion == 100,
    #     "is_urgent": Task.is_task_urgent(priority,hours,completion),
    #     "status": status
    # }


    if task.is_task_urgent():
        print("Внимание: задача срочная!")

    if task.hours > 3 and task.priority <= 2:
        print("Задачу можно запланировать на потом")
    
    return task 
    
def show_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("Список пуст")
        return

    print("\nВсе задачи:")

    for index, task in enumerate(tasks, start=1):
        print(
            f"\n{index}. {task.title}\n"
            f"   Описание: {task.description}\n"
            f"   Приоритет: {task.priority}\n"
            f"   Время выполнения: {task.hours:.2f} ч.\n"
            f"   Выполнено: {task.completion}%\n"
            f"   Статус: {task.get_status()}\n"
            f"   Важная: {task.is_important()}\n"
            f"   Долгая: {task.hours > 3}\n"
            f"   Срочная: {task.is_task_urgent()}\n"
            f"   Дедлайн: {task.deadline}"
        )

def get_all_stats(tasks: list[Task]) -> None:
    if not tasks:
        print("Список задач пуст")
        return

    for index, task in enumerate(tasks, start=1):
        print(
            f"Процент выполнения {index} задачи: "
            f"{task.completion}% - {task.get_status()}"
        )

def show_urgent_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("Список задач пуст")
        return

    urgent_found = False
    print("\nСрочные задачи:")

    for index, task in enumerate(tasks, start=1):
        if not task.is_task_urgent():
            continue

        print(
            f"\n{index}. {task.title}\n"
            f"   Приоритет: {task.priority}\n"
            f"   Время выполнения: {task.hours:.2f} ч.\n"
            f"   Выполнено: {task.completion}%\n"
            f"   Статус: {task.get_status()}"
        )

        urgent_found = True

    if not urgent_found:
        print("Срочных задач нет") 

def update_task_completion(tasks: list[Task]) -> None:
    if not tasks:
        print("Список задач пуст")
        return

    print("\nЗадачи:")

    for index, task in enumerate(tasks, start=1):
        print(
            f"{index}. {task.title} — "
            f"{task.completion}%, {task.get_status()}"
        )

    task_number = read_command(
        "\nВведите номер задачи для изменения: "
    )

    while not 1 <= task_number <= len(tasks):
        task_number = read_command(
            "Введите существующий номер задачи: "
        )

    task = tasks[task_number - 1]

    new_completion = read_command(
        "Введите новый процент выполнения: "
    )

    while not 0 <= new_completion <= 100:
        new_completion = read_command(
            "Введите процент от 0 до 100: "
        )

    task.update_completion(new_completion)

    print("Процент выполнения успешно изменён")
    print(f"Новый статус: {task.get_status()}")

    if task.is_task_urgent():
        print("Внимание: задача срочная!")

def delete_task(tasks: list[Task]) -> None:
    if not tasks:
        print("Список задач пуст")
        return

    print("\nЗадачи:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.title}")

    task_number = read_command(
        "\nВведите номер задачи для удаления: "
    )

    while not 1 <= task_number <= len(tasks):
        task_number = read_command(
            "Введите существующий номер задачи: "
        )

    removed_task = tasks.pop(task_number - 1)

    print(f"Задача «{removed_task.title}» удалена")

def get_completed_tasks(tasks):
    return [task for task in tasks if task.is_completed()]