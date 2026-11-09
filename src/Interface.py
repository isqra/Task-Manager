import tkinter as tk
from tkinter import messagebox

from AppButton import AppButton
from AppLabel import AppLabel
from AppListBox import AppListBox
from core import TaskManager
from view import update_task_list
from config import WINDOW_TITLE, WINDOW_SIZE


class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(WINDOW_TITLE)
        self.window.geometry(WINDOW_SIZE)
        self.window.configure(bg="grey")

        self.manager = TaskManager()
        self._build_ui()
        self.refresh_list()

    def _build_ui(self):
        input_frame = tk.Frame(self.window, bg="grey", padx=10, pady=10)
        input_frame.pack(fill="x")

        AppLabel(input_frame, text="Название:").pack(side="left")
        self.title_entry = tk.Entry(input_frame, width=25)
        self.title_entry.pack(side="left", padx=5)

        AppLabel(input_frame, text="Описание:").pack(side="left")
        self.desc_text = tk.Text(input_frame, width=35, height=3, wrap="word")
        self.desc_text.pack(side="left", padx=5)

        AppButton(input_frame, text="Добавить", command=self.add_task).pack(
            side="left", padx=8
        )

        list_frame = tk.Frame(self.window, bg="grey", padx=10, pady=5)
        list_frame.pack(fill="both", expand=True)

        self.listbox = AppListBox(list_frame, height=18)
        scrollbar = tk.Scrollbar(
            list_frame, orient="vertical", command=self.listbox.yview
        )
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.listbox.bind("<Double-Button-1>", lambda e: self.view_task())

        action_frame = tk.Frame(self.window, bg="grey", padx=10, pady=10)
        action_frame.pack(fill="x")

        AppButton(action_frame, text="Удалить", command=self.delete_task).pack(
            side="left", padx=5
        )
        AppButton(
            action_frame, text="Отметить выполненной", command=self.toggle_done
        ).pack(side="left", padx=5)
        AppButton(action_frame, text="Редактировать", command=self.edit_task).pack(
            side="left", padx=5
        )
        AppButton(action_frame, text="Обновить", command=self.refresh_list).pack(
            side="left", padx=5
        )

    def refresh_list(self):
        update_task_list(self.listbox, self.manager.tasks)

    def add_task(self):
        title = self.title_entry.get()
        desc = self.desc_text.get("1.0", "end-1c")
        try:
            self.manager.add_task(title, desc)
            self.title_entry.delete(0, "end")
            self.desc_text.delete(1.0, "end")
            self.refresh_list()
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e), parent=self.window)

    def view_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите задачу для просмотра", parent=self.window)
            return

        index = selection[0]
        task = self.manager.tasks[index]

        view_win = tk.Toplevel(self.window)
        view_win.title("Просмотр задачи")
        view_win.geometry("450x404")
        view_win.configure(bg="grey")
        view_win.transient(self.window)
        view_win.grab_set()

        AppLabel(view_win, text="Название:", font=("Courier New", 10, "bold")).pack(pady=(15, 2), anchor="w", padx=20)

        title_frame = tk.Frame(view_win)
        title_frame.pack(padx=20, fill="x")
        title_box = tk.Text(title_frame, wrap="word", height=2, state="normal", font=("Courier New", 10))
        title_box.insert("1.0", task["title"])
        title_box.config(state="disabled")
        title_box.pack(fill="x")

        AppLabel(view_win, text="Описание:", font=("Courier New", 10, "bold")).pack(pady=(15, 2), anchor="w", padx=20)

        desc_frame = tk.Frame(view_win)
        desc_frame.pack(padx=20, pady=(0, 10), fill="both", expand=True)
        desc_box = tk.Text(desc_frame, wrap="word", state="normal", font=("Courier New", 10))
        desc_scroll = tk.Scrollbar(desc_frame, command=desc_box.yview)
        desc_box.configure(yscrollcommand=desc_scroll.set)

        desc_text = task.get("description", "")
        if not desc_text:
            desc_text = "(Описание отсутствует)"
        desc_box.insert("1.0", desc_text)
        desc_box.config(state="disabled")

        desc_box.pack(side="left", fill="both", expand=True)
        desc_scroll.pack(side="right", fill="y")

        AppButton(view_win, text="Закрыть", command=view_win.destroy).pack(pady=(0, 15))

    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning(
                "Внимание", "Выберите задачу для удаления", parent=self.window
            )
            return
        if messagebox.askyesno(
            "Подтверждение", "Удалить выбранную задачу?", parent=self.window
        ):
            self.manager.delete_task(selection[0])
            self.refresh_list()

    def toggle_done(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning(
                "Внимание", "Выберите задачу", parent=self.window
            )
            return
        self.manager.toggle_done(selection[0])
        self.refresh_list()

    def edit_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning(
                "Внимание", "Выберите задачу для редактирования", parent=self.window
            )
            return
        index = selection[0]
        task = self.manager.tasks[index]

        edit_win = tk.Toplevel(self.window)
        edit_win.title("Редактировать задачу")
        edit_win.geometry("404x220")
        edit_win.configure(bg="grey")
        edit_win.transient(self.window)
        edit_win.grab_set()

        AppLabel(edit_win, text="Название:").pack(pady=(15, 2))
        title_entry = tk.Entry(edit_win, width=45)
        title_entry.insert(0, task["title"])
        title_entry.pack(pady=2)

        AppLabel(edit_win, text="Описание:").pack(pady=(10, 2))
        desc_entry = tk.Entry(edit_win, width=45)
        desc_entry.insert(0, task.get("description", ""))
        desc_entry.pack(pady=2)

        desc_frame = tk.Frame(edit_win)
        desc_frame.pack(padx=20, fill="both", expand=True)
        desc_box = tk.Text(desc_frame, wrap="word", width=45, height=6)
        desc_scroll = tk.Scrollbar(desc_frame, command=desc_box.yview)
        desc_box.configure(yscrollcommand=desc_scroll.set)

        desc_box.insert("1.0", task.get("description", " "))

        desc_box.pack(side="left", fill="both", expand=True)
        desc_scroll.pack(side="right", fill="y")

        def save_edit():
            try:
                self.manager.edit_task(
                    index, title_entry.get(), desc_entry.get()
                )
                edit_win.destroy()
                self.refresh_list()
            except ValueError as e:
                messagebox.showerror("Ошибка", str(e), parent=edit_win)

        AppButton(edit_win, text="Сохранить", command=save_edit).pack(pady=15)

    def run(self):
        self.window.mainloop()
