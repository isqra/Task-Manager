from AppLabel import AppLabel
from AppButton import AppButton

def show_message(parent, message, title = "Информация"):
    from tkinter import messagebox
    messagebox.showinfo(title, message, parent=parent)

def update_task_list(listbox, tasks):
    listbox.delete(0, "end")
    for task in tasks:
        status = "Y" if task.get("done") else " "
        listbox.insert("end", f"[{status}] {task["title"]}")
