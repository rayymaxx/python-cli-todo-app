class Task:
    def __init__(self, id, title, description, due_date=None, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "due_date":self.due_date,
            "completed":self.completed
        }

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"[{status}] {self.id} - {self.title} (Due: {self.due_date or 'N/A'})"