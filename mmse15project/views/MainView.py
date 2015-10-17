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
        self.container.pack()
        ttk.Separator(ttk_root, orient=tk.HORIZONTAL).pack()
        ttk.Label(ttk_root, text="© 2015 United Swedish Solutions (USS)",
                  font="-slant italic").pack()
