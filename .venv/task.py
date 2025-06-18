# This file defines tasks

class Task:
    def __init__(self, id, title, description, due_date=None, completed=False):
        self.id = id # This is used to identify the tasks in a unique way
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        self.completed = True # Marks the task as done

    def to_dict(self): # This converts the objet to a dictionary so it could be saved to the json file
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "due_date":self.due_date,
            "completed":self.completed
        }

    def __str__(self): # This is incharge of how the task looks when printed
        if self.completed:
            status = "✅"
        else:
            status = "❌"
        return f"\n[{status}] {self.id} - {self.title} (Due: {self.due_date or 'N/A'})"