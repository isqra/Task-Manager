from storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self) -> None:
        self.tasks = load_tasks()

    def add_task(self, title, description=""):
        if not title or not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        task = {
            "id" : len(self.tasks) + 1,
            "title" : title.strip(),
            "description" : description.strip(),
            "done" : False,
        }
        self.tasks.append(task)
        save_tasks(self.tasks)
        return task

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            save_tasks(self.tasks)

    def toggle_done(self, index):
        if (0 <= index < len(self.tasks)):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            save_tasks(self.tasks)

    def edit_task(self, index, title, description):
        if not (0 <= index < len(self.tasks)):
            return
        if not title or not title.strip():
            raise ValueError("Название не моежт быть пустым")
        self.tasks[index]["title"] = title.strip()
        self.tasks[index]["description"] = description.strip()
        save_tasks(self.tasks)
