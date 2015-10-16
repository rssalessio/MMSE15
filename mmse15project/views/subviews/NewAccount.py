import tkinter as tk
import tkinter.ttk as ttk


class NewAccount(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_form()

    def create_form(self):
        l1 = ttk.Label(self, text="Password:")
        l2 = ttk.Label(self, text="Email:")
        l3 = ttk.Label(self, text="Name:")
        l4 = ttk.Label(self, text="Account type:")
        l5 = ttk.Label(self, text="Account team:")
        l6 = ttk.Label(self, text="Account qualification:")
        l7 = ttk.Label(self, text="Department:")
        l8 = ttk.Label(self, text="Comment:")

        self.e1 = ttk.Entry(self)
        self.e2 = ttk.Entry(self)
        self.e3 = ttk.Entry(self)
        self.e4 = ttk.Entry(self)
        self.e5 = ttk.Entry(self)
        self.e6 = ttk.Entry(self)
        self.e7 = ttk.Entry(self)
        self.e8 = ttk.Entry(self)

        b1 = ttk.Button(self, text="Submit",
                       command=lambda: self.ctrl.newAccount_submit(self))

        l1.grid(row=0, sticky=tk.E)
        l2.grid(row=1, sticky=tk.E)
        l3.grid(row=2, sticky=tk.E)
        l4.grid(row=3, sticky=tk.E)
        l5.grid(row=4, sticky=tk.E)
        l6.grid(row=5, sticky=tk.E)
        l7.grid(row=6, sticky=tk.E)
        l8.grid(row=7, sticky=tk.E)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.e8.grid(row=7, column=1)

        b1.grid(columnspan=2)
