class TaskRepository:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def list_tasks(self, priority=None):
        if priority:
            return [t for t in self.tasks if t["priority"] == priority]
        return self.tasks

    def get_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def create_task(self, data):
        task = {
            "id": self.counter,
            "title": data["title"],
            "description": data["description"],
            "priority": data["priority"],
            "status": data["status"],
            "owner": data["owner"],
            "due_date": data["due_date"],
        }
        self.tasks.append(task)
        self.counter += 1
        return task

    def update_task(self, task_id, data):
        for task in self.tasks:
            if task["id"] == task_id:
                task.update(data)
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
        return False
