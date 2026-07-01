from functools import wraps


tasks = [
    {"title": "Изучить Python", "priority": 5, "completed": True},
    {"title": "Посмотреть видео", "priority": 2, "completed": False},
    {"title": "Написать API", "priority": 4, "completed": False},
    {"title": "Погулять", "priority": 1, "completed": True},
]



def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {function.__name__}")
        return function(*args, **kwargs)

    return wrapper

@log_call
def get_important_tasks(tasks, min_priority):
    for task in tasks:
        if task["priority"] >= min_priority:
            yield task 

@log_call
def get_uncompleted_tasks(tasks):
    for task in tasks:
        if not task["completed"]:
            yield task 

important_tasks = get_important_tasks(tasks, 4)
uncompleted_tasks = get_uncompleted_tasks(important_tasks)

for task in uncompleted_tasks:
    print(task["title"])

