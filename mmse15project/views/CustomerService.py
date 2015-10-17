import tkinter.ttk as ttk
from mmse15project.views.subviews.NewClientRecord import NewClientRecord
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
        f1 = NewClientRecord(n, self.model, self.ctrl)
        f2 = NewRequestForEvent(n, self.model, self.ctrl)
        f3 = ttk.Frame(n)
        f4 = ttk.Frame(n)
        n.add(f1, text="Create client")
        n.add(f2, text="Create Request for Event")
        n.add(f3, text="Search for clients")
        n.add(f4, text="Search for Request for Event")