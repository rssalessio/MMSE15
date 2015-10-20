import tkinter.ttk as ttk
from mmse15project.views.Config import Config
from mmse15project.views.GenericMethods import get_header
from mmse15project.views.subviews.NewAccount import NewAccount


# AccountTeam view for TopManagement
class TopManagement(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_team, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_team = acc_team
        self.acc_type = acc_type
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        self.ctrl.clear_frame(self)
        get_header(self, "Config", lambda: self.config())
        n = ttk.Notebook(self)
        n.grid(row=1, columnspan=2)
        f1 = NewAccount(n, self.model, self.ctrl)
        n.add(f1, text="New account")

    def config(self):
        self.ctrl.clear_frame(self)
        get_header(self, "General", lambda: self.create_widgets())
        c = Config(self, self.model, self. ctrl)
        c.grid(row=1, columnspan=2)
