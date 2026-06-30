from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str


@dataclass
class Task:
    title: str
    author: User


user = User("Лев","Почта")
task = Task("Изучить ООП",user)

print(f"Название задачи: {task.title}")
print(f"Автор: {task.author.name}")
print(f"Email: {task.author.email}")