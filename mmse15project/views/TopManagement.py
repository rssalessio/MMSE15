import tkinter.ttk as ttk
from mmse15project.views.subviews.NewAccount import NewAccount


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
        user_info = "Top Management, " + self.acc_type + " - logged in as " + self.user
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()
        f1 = NewAccount(n, self.model, self.ctrl)
        f2 = NewAccount(n, self.model, self.ctrl)
        n.add(f1, text='Create new account')
        n.add(f2, text='Create new account')
