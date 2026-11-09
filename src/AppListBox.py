import tkinter as tk

class AppListBox(tk.Listbox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            font = ("Courier New", 11),
            selectbackground = "#36526d",
            selectforeground = "white",
            activestyle = "none",
            borderwidth = 0,
            highlightthickness = 0
        )
