import tkinter as tk
import tkinter.ttk as ttk


class MainView(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mailman")
        self.resizable(tk.FALSE, tk.FALSE)
        self.attributes("-topmost", True)

        self.container = tk.Frame(self)
        separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        company = tk.Label(self, text="© 2015 United Swedish Solutions (USS)",
                           font="-slant italic")

        self.container.grid(row=0, column=0)
        separator.grid(row=1, sticky="ew")  # east to west
        company.grid(row=2, column=0)
