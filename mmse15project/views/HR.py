import tkinter.ttk as ttk
from mmse15project.views.subviews.SearchEmployee import *

# AccountTeam view for HR
class HR(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_team, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_team = acc_team
        self.acc_type = acc_type
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        container = ttk.Frame(self)
        container.pack()
        user_info = "HR, %s — %s" % (self.acc_type, self.user)
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()
        f1 = SearchEmployee(n, self.model, self.ctrl)
        f2 = ttk.Frame(n)
        f3 = ttk.Frame(n)
        n.add(f1, text="Search employee")
        n.add(f2, text="Pending requests")
        n.add(f3, text="Publish job advertisement")