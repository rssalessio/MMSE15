import tkinter.ttk as ttk
from mmse15project.views.subviews.NewAccount import NewAccount


# AccountTeam view for TopManagement
class TopManagement(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_type = acc_type
        self.user = user
        self.create_view()

    def create_view(self):
        container = ttk.Frame(self)
        container.pack()
        user_info = "Top Management - logged in as " + self.user
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()
        f1 = NewAccount(n, self.model, self.ctrl)
        f2 = ttk.Frame(self)
        n.add(f1, text='Create new account')
        n.add(f2, text='Two')
