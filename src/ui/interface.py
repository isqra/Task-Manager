import tkinter as tk
from frame import AppFrame

class Interface:
    def __init__(self, window_h=444, window_w=444):
        self.root = tk.Tk()
        self.root_w = window_w
        self.root_h = window_h
        self.root.geometry(f"{self.root_w}x{self.root_h}")

        self.frames = {}
        self.buttons = []

        self.create_interface()

        self.root.mainloop()

    def create_interface(self):
        self.create_frame(["Menu", "Tasks"])
        self.create_buttons()

    def create_frame(self, name_frame):
        frame = AppFrame(self.root, "black", self.root_w, self.root_h)
        for i in range(len(name_frame)):
            self.frames[name_frame[i]] = frame


    def create_buttons(self):
        pass


interface = Interface()