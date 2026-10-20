import tkinter as tk

class AppFrame(tk.Frame):
    def __init__(self, master, color, width, height):
        super().__init__(master, background=color, width=width, height=height)
        self.background = color
        self.master = master
        self.width = width
        self.height = height
        self.pack_propagate(False)
        self.pack()
        print(color)
