import tkinter.ttk as ttk
from mmse15project.views.Config import Config
from mmse15project.views.GenericMethods import get_header
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
        self.ctrl.clear_frame(self)
        get_header(self, "Config", lambda: self.config())
        n = ttk.Notebook(self)
        n.grid(row=1, columnspan=2)
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

    def config(self):
        self.ctrl.clear_frame(self)
        get_header(self, "General", lambda: self.create_widgets())
        c = Config(self, self.model, self. ctrl)
        c.grid(row=1, columnspan=2)

