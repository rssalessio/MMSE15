import tkinter.ttk as ttk
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails
from mmse15project.views.subviews.PendingRecruitmentRequest import PendingRecruitmentRequest
from mmse15project.views.subviews.SearchRecruitmentRequest import SearchRecruitmentRequest

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
        f1 = PendingRecruitmentRequest(n, self.model, self.ctrl)
        f2 = SearchRecruitmentRequest(n, self.model, self.ctrl)
        f3 = SearchRequest(n, self.model, self.ctrl)
        f4 = SearchRequestDetails(n, self.model, self.ctrl)
        n.add(f1, text="Pending recruitments", sticky="NS")
        n.add(f2, text="View recruitment", sticky="NS")
        n.add(f3, text="View request", sticky="NS")
        n.add(f4, text="View request details", sticky="NS")