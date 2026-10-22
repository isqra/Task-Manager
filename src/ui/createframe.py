import tkinter as tk


class AppFrame(tk.Frame):
    """Фрейм с цветом фона и необязательным фиксированным размером."""

    def __init__(self, master, color="#f0f0f0", width=None, height=None, **kwargs):
        super().__init__(master, bg=color, width=width or 0, height=height or 0, **kwargs)
        self.background = color
        if width and height:
            self.pack_propagate(False)

    def show(self, **pack_options):
        self.pack(**pack_options)

    def hide(self):
        self.pack_forget()