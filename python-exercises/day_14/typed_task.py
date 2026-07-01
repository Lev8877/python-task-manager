from dataclasses import dataclass


@dataclass
class Task:
    title: str
    description: str 
    priority: int 
    hours: int 
    completion: int = 0
    deadline: str | None = None 

    def is_completed(self) -> bool:
        return self.completion == 100
    
    def update_completion(self, new_completion: int) -> None:
        self.completion = new_completion

    def is_important(self) -> bool:
        return self.priority >= 4
    
    def __str__(self) -> str:
        return f"{self.title} — {self.completion}%"
    
    def has_deadline(self) -> bool:
        return self.deadline is not None 

