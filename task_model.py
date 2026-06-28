class Task:
    def __init__(self,title, description, priority, hours, completion):
        self.title = title 
        self.description = description
        self.priority = priority
        self.hours = hours
        self.completion = completion

    def is_completed(self):
        return self.completion == 100
    
    def update_completion(self, new_completion):
        self.completion = new_completion

    def is_important(self):
        return self.priority >= 4
    

