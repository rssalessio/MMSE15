import tkinter as tk
import tkinter.ttk as ttk


# MainView is the root view, have a container for AccountTeam views
class MainView(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mailman")
        self.resizable(tk.FALSE, tk.FALSE)
        self.attributes("-topmost", True)

        ttk_root = ttk.Frame(self)
        ttk_root.pack()

        self.container = ttk.Frame(ttk_root)
        separator = ttk.Separator(ttk_root, orient=tk.HORIZONTAL)
        company = ttk.Label(ttk_root, text="© 2015 United Swedish Solutions (USS)",
                           font="-slant italic")

        self.container.grid(row=0, column=0)
        separator.grid(row=1, sticky="ew")  # east to west
        company.grid(row=2, column=0)
