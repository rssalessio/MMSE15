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
        self.create_widgets()

    def create_widgets(self):
        container = ttk.Frame(self)
        container.pack()
        user_info = "Top Management, %s — %s" % (self.acc_type, self.user)
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()
        f1 = NewAccount(n, self.model, self.ctrl)
        n.add(f1, text="New account")