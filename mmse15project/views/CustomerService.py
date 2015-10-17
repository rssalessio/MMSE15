import tkinter.ttk as ttk
import tkinter as tk
from mmse15project.views.subviews.SearchClientRecord import SearchClientRecord
from mmse15project.views.subviews.NewClientRecord import NewClientRecord
from mmse15project.views.subviews.SearchRequestForEvent import SearchRequestForEvent
from mmse15project.views.subviews.NewRequestForEvent import NewRequestForEvent

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
        user_info = "Customer Service - logged in as " + self.user
        ttk.Label(container, text=user_info).pack()
        n = ttk.Notebook(container)
        n.pack()
        f1 = SearchClientRecord(n, self.model, self.ctrl)
        f2 = NewClientRecord(n, self.model, self.ctrl)
        f3 = SearchRequestForEvent(n, self.model, self.ctrl)
        f4 = NewRequestForEvent(n, self.model, self.ctrl)
        n.add(f1, text="Search for client", sticky="NS")
        n.add(f2, text="Create new client", sticky="NS")
        n.add(f3, text="Search for Request for Event", sticky="NS")
        n.add(f4, text="Create new Request for Event", sticky="NS")
