import tkinter.ttk as ttk
from mmse15project.model.Task import TaskStatus
from mmse15project.model.Task import TaskPriority


class PendingFinancialRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        b1 = ttk.Button(self, text="Update",
                       command=lambda: self.ctrl.pending_financial_request_update(self))
        b1.grid(row=0)

        self.update = self.Update(self, self.model, self.ctrl)
        self.update.grid(row=1)
        self.update.create_widgets()

    class Update(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            acc_type = self.master.master.master.master.acc_type
            user = self.master.master.master.master.user

            financials = self.model.financial_request_db.getByStatus(1)
            if len(financials) == 0:
                ttk.Label(self, text="No pending financial requests").grid()
                return
            ttk.Label(self, text="FinancialID:").grid(row=0, sticky="E")
            ttk.Label(self, text="Department").grid(row=0, column=1, sticky="W")
            row = 1
            for f in financials:
                ttk.Label(self, text=str(f.id) + ":").grid(row=row, sticky="E")
                ttk.Label(self, text=f.department).grid(row=row, column=1, sticky="W")
                row += 1
