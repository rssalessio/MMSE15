import tkinter.ttk as ttk
from mmse15project.views.Config import Config
from mmse15project.views.GenericMethods import get_header
from mmse15project.views.subviews.NewFinancialRequest import NewFinancialRequest
from mmse15project.views.subviews.NewRecruitmentRequest import NewRecruitmentRequest
from mmse15project.views.subviews.NewTask import NewTask
from mmse15project.views.subviews.PendingTasks import PendingTasks
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails
from mmse15project.views.subviews.SearchTasks import SearchTasks


# AccountTeam view for Production
class Production(ttk.Frame):
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
        f1 = PendingTasks(n, self.model, self.ctrl)
        n.add(f1, text="Active tasks", sticky="NS")
        if self.acc_type == "Manager":
            f2 = SearchRequest(n, self.model, self.ctrl)
            f3 = SearchRequestDetails(n, self.model, self.ctrl)
            n.add(f2, text="View request", sticky="NS")
            n.add(f3, text="View request details", sticky="NS")

        f4 = SearchTasks(n, self.model, self.ctrl)
        n.add(f4, text="View task", sticky="NS")

        if self.acc_type == "Manager":
            f5 = NewRecruitmentRequest(n, self.model, self.ctrl)
            f6 = NewFinancialRequest(n, self.model, self.ctrl)
            f7 = NewTask(n, self.model, self.ctrl)
            n.add(f5, text="New recruitment", sticky="NS")
            n.add(f6, text="New financial", sticky="NS")
            n.add(f7, text="New task", sticky="NS")

    def config(self):
        self.ctrl.clear_frame(self)
        get_header(self, "General", lambda: self.create_widgets())
        c = Config(self, self.model, self. ctrl)
        c.grid(row=1, columnspan=2)
