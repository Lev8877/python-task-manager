from dataclasses import dataclass

@dataclass
class Task:
    title: str
    description: str
    priority: int
    hours: int
    completion: int = 0

    def is_completed(self):
        return self.completion == 100 
    
    def update_completion(self,new_completion):
        self.completion = new_completion

    def is_important(self):
        return self.priority >= 4
    
    def __str__(self):
        return f"{self.title} - {self.completion}%"
    

task = Task(
    title="Изучить ООП",
    description="Разобрать dataclass",
    priority=5,
    hours=3,
    completion=20,
)

print(task)
print(task.is_important())
print(task.is_completed())
task.update_completion(100)
print(task)