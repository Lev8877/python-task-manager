from dataclasses import dataclass


@dataclass
class Task:
    title: str
    description: str 
    priority: int 
    hours: int 
    completion: int = 0
    deadline: str | None = None

    def is_completed(self):
        return self.completion == 100
    
    def update_completion(self, new_completion):
        self.completion = new_completion

    def is_important(self):
        return self.priority >= 4
    
    def get_status(self):
        if self.completion == 0:
            return "Задача не начата"
        elif self.completion == 100:
            return "Задача завершена"
        return "Задача в процессе"
    
    def is_task_urgent(self):
        return (
        self.priority == 5
        or (self.priority >= 4 and self.hours <= 2)
    ) and self.completion != 100
    
    def __str__(self):
        return f"{self.title} — {self.completion}%"