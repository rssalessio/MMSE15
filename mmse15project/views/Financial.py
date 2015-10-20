import tkinter.ttk as ttk
from mmse15project.views.Config import Config
from mmse15project.views.GenericMethods import get_header
from mmse15project.views.subviews.NewDiscount import NewDiscount
from mmse15project.views.subviews.PendingRequests import PendingRequests
from mmse15project.views.subviews.PendingFinancialRequest import PendingFinancialRequest
from mmse15project.views.subviews.SearchClient import SearchClient
from mmse15project.views.subviews.SearchDiscount import SearchDiscount
from mmse15project.views.subviews.SearchFinancialRequest import SearchFinancialRequest
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails


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
        self.ctrl.clear_frame(self)
        get_header(self, "Config", lambda: self.config())
        n = ttk.Notebook(self)
        n.grid(row=1, columnspan=2)

        if self.acc_type == "Manager":
            f1 = PendingRequests(n, self.model, self.ctrl)
            f2 = PendingFinancialRequest(n, self.model, self.ctrl)
            f3 = SearchClient(n, self.model, self.ctrl)
            f4 = SearchRequest(n, self.model, self.ctrl)
            f5 = SearchRequestDetails(n, self.model, self.ctrl)
            f6 = SearchFinancialRequest(n, self.model, self.ctrl)
            f7 = NewDiscount(n, self.model, self.ctrl)
            f8 = SearchDiscount(n, self.model, self.ctrl)
            n.add(f1, text="Pending requests", sticky="NS")
            n.add(f2, text="Pending financials", sticky="NS")
            n.add(f3, text="View client", sticky="NS")
            n.add(f4, text="View request", sticky="NS")
            n.add(f5, text="View request details", sticky="NS")
            n.add(f6, text="View financial", sticky="NS")
            n.add(f7, text="New discount", sticky="NS")
            n.add(f8, text="View discount", sticky="NS")

    def config(self):
        self.ctrl.clear_frame(self)
        get_header(self, "General", lambda: self.create_widgets())
        c = Config(self, self.model, self. ctrl)
        c.grid(row=1, columnspan=2)
