import json
from pathlib import Path
from dataclasses import asdict
from task_model import Task


path = Path(__file__).parent / "tasks.json"


def save_tasks(tasks):
    task_data = [asdict(task) for task in tasks] #Преобразовываем объекты класса в словари
    with open(path, "w", encoding="utf-8") as file:
        json.dump(task_data, file, ensure_ascii=False, indent=4)


def load_tasks():
    try:
        with open(path, "r", encoding="utf-8") as file:
            task_data = json.load(file)
        return [Task(**item) for item in task_data]

    except FileNotFoundError:
        print("Файл JSON не найден. Создан пустой список задач")
        return []

    except json.JSONDecodeError:
        print("Файл JSON пустой или повреждён. Создан пустой список задач")
        return []