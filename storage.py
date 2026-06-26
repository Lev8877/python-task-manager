import json
from pathlib import Path


path = Path(__file__).parent / "tasks.json"


def save_tasks(tasks):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def load_tasks():
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Файл JSON не найден. Создан пустой список задач")
        return []

    except json.JSONDecodeError:
        print("Файл JSON пустой или повреждён. Создан пустой список задач")
        return []