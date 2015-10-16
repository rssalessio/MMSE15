import tkinter as tk
import tkinter.ttk as ttk
from mmse15project.views.NewAccount import NewAccount


class ManagementStaff(tk.Frame):
    def __init__(self, master, model, ctrl):
        tk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_view()

    def create_view(self):
        container = ttk.Frame(self)
        container.pack()
        ttk.Label(container, text="Management Staff, logged in as [name]").pack()
        n = ttk.Notebook(container)
        n.pack()
        f1 = NewAccount(n, self.model, self.ctrl)
        f2 = NewAccount(n, self.model, self.ctrl)
        n.add(f1, text='Create new account')
        n.add(f2, text='Create new account')
