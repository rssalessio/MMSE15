import tkinter as tk
import tkinter.ttk as ttk


# Start up view
class Login(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.auth()

    def auth(self):
        ttk.Label(self, text="User:").grid(row=0, sticky=tk.E)
        ttk.Label(self, text="Pass:").grid(row=1, sticky=tk.E)

        self.e1 = ttk.Entry(self)  # User
        self.e1.grid(row=0, column=1)
        self.e2 = ttk.Entry(self, show="*")  # Pass
        self.e2.grid(row=1, column=1)

        b1 = ttk.Button(self, text="Login",
                       command=lambda: self.ctrl.login_auth(self))
        b1.grid(columnspan=2)

    def get_all(self):
        return [self.e1.get(), self.e2.get()]

    def fail(self):
        l1 = ttk.Label(self, text="Authentication failed")
        b1 = ttk.Button(self, text="Try again",
                       command=lambda: self.ctrl.login_try_again(self))
        b2 = ttk.Button(self, text="Quit",
                       command=lambda: self.ctrl.login_quit())
        l1.grid(row=0, columnspan=2)
        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
