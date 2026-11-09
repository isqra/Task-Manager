import tkinter as tk

class AppLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Courier New", 10), bg = "grey")
