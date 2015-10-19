import tkinter.ttk as ttk
from mmse15project.views.subviews.MakeDiscount import *
from mmse15project.views.subviews.SearchClient import *
from mmse15project.views.subviews.SearchRequest import *
# AccountTeam view for Financial
class Financial(ttk.Frame):
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
        user_info = "Financial, %s — %s" % (self.acc_type, self.user)
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()

        f1 = ttk.Frame(n)
        f2 = SearchClient(n, self.model, self.ctrl)
        f3 = SearchRequest(n, self.model, self.ctrl)
        f4 = ttk.Frame(n)
        f5 = MakeDiscount(n, self.model, self.ctrl)
        f6 = ttk.Frame(n)
        n.add(f1, text="Pending requests", sticky="NS")
        n.add(f2, text="Search client", sticky="NS")
        n.add(f3, text="Search request", sticky="NS")
        n.add(f4, text="Search discount", sticky="NS")
        n.add(f5, text="Make discount", sticky="NS")
        n.add(f6, text="Search employee", sticky="NS")
