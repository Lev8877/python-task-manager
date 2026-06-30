from dataclasses import dataclass
@dataclass
class Task:
    title: str 

    def show_info(self):
        print(f"Рабочая задача: {self.title}")


class WorkTask(Task):
    def __init__(self, title, company):
        super().__init__(title)
        self.company = company

    def show_info(self):
        print(f"Рабочая задача: {self.title}")
        print(f"Компания: {self.company}")


work_task = WorkTask("Подготовить отчёт","OpenAI")
work_task.show_info()