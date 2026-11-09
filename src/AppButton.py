import tkinter as tk

class AppButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            font = ("Courier New", 10),
            bg = "#36526d",
            fg = "white",
            relief = "flat",
            padx = 10,
            pady = 5,
            cursor = "hand2",
        )
