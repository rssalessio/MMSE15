import tkinter.ttk as ttk
from mmse15project.views.subviews.SearchClient import SearchClient
from mmse15project.views.subviews.NewClient import NewClient
from mmse15project.views.subviews.SearchRequest import SearchRequest
from mmse15project.views.subviews.NewRequest import NewRequest


# AccountTeam view for CustomerService
class CustomerService(ttk.Frame):
    def __init__(self, master, model, ctrl, acc_type, user):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.acc_type = acc_type
        self.user = user
        self.create_view()

    def create_view(self):
        container = ttk.Frame(self)
        container.pack()
        user_info = "Customer Service, %s — %s" % (self.acc_type, self.user)
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()
        f1 = SearchClient(n, self.model, self.ctrl)
        f2 = NewClient(n, self.model, self.ctrl)
        f3 = SearchRequest(n, self.model, self.ctrl)
        f4 = NewRequest(n, self.model, self.ctrl)
        n.add(f1, text="Search for client", sticky="NS")
        n.add(f2, text="Create new client", sticky="NS")
        n.add(f3, text="Search for request for event", sticky="NS")
        n.add(f4, text="Create new request for event", sticky="NS")
