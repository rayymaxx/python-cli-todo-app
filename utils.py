# This file handles saving tasks to or from the json file where the data is stored permanently

from task import Task
import os
import json

tasks_f = "tasks.json"

def load_tasks():
    if not os.path.exists(tasks_f):
        return []
    with open(tasks_f, "r") as file:
        data = json.load(file)
        return [Task(**task) for task in data]
    
def save_tasks(tasks):
    with open(tasks_f, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=2)

def generate_task_id(tasks):
    return max([task.id for task in tasks], default=0) + 1
