import tkinter.ttk as ttk
from mmse15project.views.subviews.MakeDiscount import MakeDiscount
from mmse15project.views.subviews.SearchClient import SearchClient
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchEmployee import SearchEmployee
from mmse15project.views.subviews.SearchDiscount import SearchDiscount
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails
from mmse15project.views.subviews.PendingRequests import PendingRequests


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

        if self.acc_type == "Manager":
            f1 = PendingRequests(n, self.model, self.ctrl)
            f2 = SearchClient(n, self.model, self.ctrl)
            f3 = SearchRequest(n, self.model, self.ctrl)
            f4 = SearchRequestDetails(n, self.model, self.ctrl)
            n.add(f1, text="Pending requests")
            n.add(f2, text="Search client", sticky="NS")
            n.add(f3, text="Search request", sticky="NS")
            n.add(f4, text="Search request details", sticky="NS")

        #f1 = ttk.Frame(n)
        #f2 = SearchClient(n, self.model, self.ctrl)
        #f3 = SearchRequest(n, self.model, self.ctrl)
        #f4 = SearchDiscount(n, self.model, self.ctrl)
        #f5 = MakeDiscount(n, self.model, self.ctrl)
        #f6 = SearchEmployee(n,self.model,self.ctrl)
        #n.add(f1, text="Pending requests", sticky="NS")
        #n.add(f2, text="Search client", sticky="NS")
        #n.add(f3, text="Search request", sticky="NS")
        #n.add(f4, text="Search discount", sticky="NS")
        #n.add(f5, text="Make discount", sticky="NS")
        #n.add(f6, text="Search employee", sticky="NS")
