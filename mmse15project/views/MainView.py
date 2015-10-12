import tkinter as tk
import tkinter.ttk as ttk

__author__ = 'tobias'


class MainView(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mailman")
        self.attributes("-topmost", True)

        self.container = tk.Frame(self)
        company = tk.Label(self, text="© 2015 Swedish Events Planners SEP", font="-slant italic")
        separator = ttk.Separator(self, orient=tk.HORIZONTAL)

        self.container.grid(row=0, column=0)
        separator.grid(sticky="ew")  # east to west
        company.grid(row=2, column=0)