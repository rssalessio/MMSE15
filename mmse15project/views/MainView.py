import tkinter as tk
import tkinter.ttk as ttk


# MainView is the root view, have a container for AccountTeam views
class MainView(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mailman")
        self.resizable(tk.FALSE, tk.FALSE)
        self.attributes("-topmost", True)

        self.container = ttk.Frame(self)
        self.container.grid(row=0, sticky="WE")
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=1, sticky="WE")
        ttk.Label(self, text="© 2015 United Swedish Solutions (USS)",
                  font="-slant italic").grid(row=2, sticky="WE")
