import tkinter.ttk as ttk
import tkinter as tk


# Form for creating a new account
class NewAccount(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Full name:").grid(row=0, sticky="E")
        ttk.Label(self, text="Username:").grid(row=1, sticky="E")
        ttk.Label(self, text="Password:").grid(row=2, sticky="E")
        ttk.Label(self, text="Account team:").grid(row=3, sticky="E")
        ttk.Label(self, text="Account type:").grid(row=4, sticky="E")
        ttk.Label(self, text="Job title:").grid(row=5, sticky="E")
        ttk.Label(self, text="Comment:").grid(row=6, sticky="E")

        self.e1 = ttk.Entry(self)  # Full name
        self.e1.grid(row=0, column=1)
        self.e2 = ttk.Entry(self)  # Username
        self.e2.grid(row=1, column=1)
        self.e3 = ttk.Entry(self)  # Password
        self.e3.grid(row=2, column=1)

        self.e4 = tk.StringVar(self)  # Account team
        acc_teams=["Administration", "HR", "Customer Service", "Marketing",
                   "Financial", "Production", "Service", "Top Management"]
        self.e4.set(acc_teams[0])
        ttk.OptionMenu(self, self.e4, self.e4.get(), *acc_teams).grid(row=3, column=1, sticky="E")

        self.e5 = tk.StringVar(self)  # Account type
        acc_types=["Employee", "Senior", "Manager"]
        self.e5.set(acc_types[0])
        ttk.OptionMenu(self, self.e5, self.e5.get(), *acc_types).grid(row=4, column=1, sticky="E")

        self.e6 = ttk.Entry(self)  # Job title
        self.e6.grid(row=5, column=1)
        self.e7 = ttk.Entry(self)  # Comment
        self.e7.grid(row=6, column=1)

        b1 = ttk.Button(self, text="Submit",
                       command=lambda: self.ctrl.new_account_submit(self))
        b1.grid(columnspan=2)

    def get_all(self):
        return [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),
                self.e5.get(), self.e6.get(), self.e7.get()]
