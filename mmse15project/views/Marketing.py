import tkinter.ttk as ttk
from mmse15project.views.subviews.SearchClient import SearchClient
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.SearchRequestDetails import SearchRequestDetails


# AccountTeam view for Marketing
class Marketing(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_team, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_team = acc_team
        self.acc_type = acc_type
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        user_info = "Marketing, " + self.acc_type + " - logged in as " + self.user
        ttk.Label(self, text=user_info).pack()
        n = ttk.Notebook(self)
        n.pack()
        f2 = SearchClient(n, self.model, self.ctrl)
        f3 = SearchRequest(n, self.model, self.ctrl)
        f4 = SearchRequestDetails(n, self.model, self.ctrl)
        n.add(f2, text="View client", sticky="NS")
        n.add(f3, text="View request", sticky="NS")
        n.add(f4, text="View request details", sticky="NS")
