import tkinter.ttk as ttk
from mmse15project.model.Account import AccountTeam, AccountType


class Config(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        account = self.model.account_db.getByEmail(self.master.user)
        if account is False:
            ttk.Label(self, text="User account not found").grid()
            return

        ttk.Label(self, text="Full name:").grid(row=0, sticky="E")
        ttk.Label(self, text="Username:").grid(row=1, sticky="E")
        ttk.Label(self, text="Password:").grid(row=2, sticky="E")
        ttk.Label(self, text="Account team:").grid(row=3, sticky="E")
        ttk.Label(self, text="Account type:").grid(row=4, sticky="E")
        ttk.Label(self, text="Job title:").grid(row=5, sticky="E")
        ttk.Label(self, text="Comment:").grid(row=6, sticky="E")

        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)
        self.e1.insert(0, account.getName())

        self.e2 = account.getEmail()
        ttk.Label(self, text=self.e2).grid(row=1, column=1, sticky="W")

        self.e3 = ttk.Entry(self, show="*")
        self.e3.grid(row=2, column=1)
        self.e3.insert(0, account.getPassword())

        self.e4 = account.getAccountTeam()
        ttk.Label(self, text=AccountTeam(self.e4).name).grid(row=3, column=1, sticky="W")

        self.e5 = account.getAccountType()
        ttk.Label(self, text=AccountType(self.e5).name).grid(row=4, column=1, sticky="W")

        self.e6 = account.getDepartment()
        ttk.Label(self, text=self.e6).grid(row=5, column=1, sticky="W")

        self.e7 = ttk.Entry(self)
        self.e7.grid(row=6, column=1)
        self.e7.insert(0, account.getComment())

        b1 = ttk.Button(self, text="Save", command=lambda: self.ctrl.config_save(self))
        b1.grid(columnspan=2)

    def get_all(self):
        return [self.e1.get(), self.e2, self.e3.get(), self.e4, self.e5, self.e6, self.e7.get()]

