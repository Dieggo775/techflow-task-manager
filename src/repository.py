# src/repository.py
from datetime import datetime

class TaskRepository:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def list_tasks(self, priority=None):
        if priority:
            return [t for t in self.tasks if t["priority"] == priority]
        return self.tasks

    def create_task(self, data):
        task = {
            "id": self.counter,
            "title": data["title"],
            "description": data["description"],
            "priority": data["priority"],  # e.g., High, Medium, Low
            "status": data["status"],      # To Do, In Progress, Done
            "owner": data["owner"],
            "due_date": data.get("due_date")  # mudança de escopo
        }
        self.tasks.append(task)
        self.counter += 1
        return task

    def update_task(self, task_id, data):
        for t in self.tasks:
            if t["id"] == task_id:
                t.update({k: v for k, v in data.items() if k in t})
                return t
        return None

    def delete_task(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                self.tasks.remove(t)
                return True
        return False
