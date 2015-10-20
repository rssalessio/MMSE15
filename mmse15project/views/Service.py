import tkinter.ttk as ttk
from mmse15project.views.subviews.NewFinancialRequest import NewFinancialRequest
from mmse15project.views.subviews.NewRecruitmentRequest import NewRecruitmentRequest
from mmse15project.views.subviews.NewTask import NewTask
from mmse15project.views.subviews.PendingTasks import PendingTasks
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails
from mmse15project.views.subviews.SearchTasks import SearchTasks


# AccountTeam view for Service
class Service(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_team, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_team = acc_team
        self.acc_type = acc_type
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        user_info = "Service, %s — %s" % (self.acc_type, self.user)
        ttk.Label(self, text=user_info).pack()
        n = ttk.Notebook(self)
        n.pack()
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
