import tkinter.ttk as ttk
from mmse15project.views.subviews.NewClient import NewClient
from mmse15project.views.subviews.NewRequest import NewRequest
from mmse15project.views.subviews.NewRequestDetails import NewRequestDetails
from mmse15project.views.subviews.PendingRequests import PendingRequests
from mmse15project.views.subviews.SearchClient import SearchClient
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails


# AccountTeam view for CustomerService
class CustomerService(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_team, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_team = acc_team
        self.acc_type = acc_type
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        user_info = "Customer Service, %s — %s" % (self.acc_type, self.user)
        ttk.Label(self, text=user_info).pack()
        n = ttk.Notebook(self)
        n.pack()
        if self.acc_type == "Senior":
            f1 = PendingRequests(n, self.model, self.ctrl)
            n.add(f1, text="Pending requests", sticky="NS")
        f2 = SearchClient(n, self.model, self.ctrl)
        f3 = SearchRequest(n, self.model, self.ctrl)
        f4 = SearchRequestDetails(n, self.model, self.ctrl)
        n.add(f2, text="View client", sticky="NS")
        n.add(f3, text="View request", sticky="NS")
        n.add(f4, text="View request details", sticky="NS")
        if self.acc_type == "Employee":
            f5 = NewClient(n, self.model, self.ctrl)
            f6 = NewRequest(n, self.model, self.ctrl)
            n.add(f5, text="New client", sticky="NS")
            n.add(f6, text="New request", sticky="NS")
        if self.acc_type == "Senior":
            f7 = NewRequestDetails(n, self.model, self.ctrl)
            n.add(f7, text="New request details", sticky="NS")
