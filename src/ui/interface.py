import tkinter as tk

from .createframe import AppFrame
from .mathcore import operations, calculate

digits_buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
operation_buttons = ["*", "%", "+", "-", "="]


class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("404x404")
        self.window.resizable(False, False)
        self.tokens = []
        self.current_digit = ""
        self.result_show = False
        self._build_display()
        self._build_buttons()

    def _build_display(self):
        frame = AppFrame(self.window, color="#ffffff")
        frame.pack(fill="x", padx=10, pady=10)

        self.text_input = tk.Label(
            frame,
            text="",
            font=("Courier New", 24),
            anchor="e",
            bg="white",
            height=2,
        )
        self.text_input.pack(fill="x")

    def _build_buttons(self):
        frame = AppFrame(self.window, color="grey")
        frame.pack(expand=True, fill="both", padx=10, pady=10)
        for column in range(4):
            frame.columnconfigure(column, weight=1)
        for row in range(5):
            frame.rowconfigure(row, weight=1)

        # тут кнопки цифр
        for index, digit in enumerate(digits_buttons):
            row, column = divmod(index, 3)
            button = tk.Button(
                frame,
                text=digit,
                font=("Courier New", 18),
                command=lambda value=digit: self.press(value),
            )
            button.grid(row=row, column=column, sticky="nsew", padx=3, pady=3)

        # операции + - и так далее
        for row, operator in enumerate(operation_buttons):
            button = tk.Button(
                frame,
                text=operator,
                font=("Courier New", 18),
                command=lambda value=operator: self.press(value),
            )
            button.grid(row=row, column=3, sticky="nsew", padx=3, pady=3)

    def press(self, value):
        if value.isdigit():
            if self.result_show:
                self.current_digit = ""
                self.result_show = False
            self.current_digit += value
            self._show()
        elif value == "=":
            self._equal()
        else:
            self._operator(value)
            self._show()

    def _operator(self, operator):
        self.result_show = False
        if self.current_digit:
            self.tokens.append(self.current_digit)
            self.tokens.append(operator)
            self.current_digit = ""
        elif self.tokens:
            self.tokens[-1] = operator

    def _equal(self):
        if self.current_digit:
            self.tokens.append(self.current_digit)
            self.current_digit = ""

        if self.tokens and self.tokens[-1] in operations:
            self.tokens.pop()

        if not self.tokens:
            return

        result = calculate(self.tokens)
        self.tokens = []

        if result == "ERROR":
            self.text_input.config(text=result)
            self.window.after(1500, self._show)
            return

        self.current_digit = result
        self.result_shown = True
        self._show()

    def _show(self):
        parts = self.tokens + ([self.current_digit] if self.current_digit else [])
        self.text_input.config(text=" ".join(parts))