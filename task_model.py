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
    
    def update_completion(self, new_completion):
        self.completion = new_completion

    def is_important(self):
        return self.priority >= 4
    
    def __str__(self):
        return f"{self.title} — {self.completion}%"
    

