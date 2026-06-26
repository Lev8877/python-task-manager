import json
from pathlib import Path

path = Path(__file__).parent / "tasks.json"

def save_tasks(tasks):
    with open(path,"w",encoding="utf-8") as file:
        json.dump(tasks,file,ensure_ascii=False,indent=4)
    return 

def load_tasks():
    with open(path,"r",encoding="utf-8") as file:
        data = json.load(file)
    return data 

