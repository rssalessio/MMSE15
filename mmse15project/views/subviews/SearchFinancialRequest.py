import tkinter.ttk as ttk
from mmse15project.model.FinancialRequest import FinancialRequestStatus


class SearchFinancialRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="FinancialID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Get",
                        command=lambda: self.ctrl.search_financial_request_get(self))
        b1.grid(row=1, columnspan=2)

        self.result = self.Result(self, self.model, self.ctrl)
        self.result.grid(row=2, columnspan=2)

    class Result(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)

            wanted = int(self.master.e1.get())
            f = self.model.financial_request_db.getByID(wanted)
            self.f = f

            if f is False:
                ttk.Label(self, text="No such financial request").grid(row=0, columnspan=2)
            else:
                ttk.Label(self, text="Requesting department:").grid(row=0, sticky="E")
                ttk.Label(self, text=f.department).grid(row=0, column=1, sticky="W")

                ttk.Label(self, text="RequestID:").grid(row=1, sticky="E")
                ttk.Label(self, text=str(f.requestID)).grid(row=1, column=1, sticky="W")

                ttk.Label(self, text="Required amount:").grid(row=2, sticky="E")
                ttk.Label(self, text=str(f.amount)).grid(row=2, column=1, sticky="W")

                ttk.Label(self, text="Reason:").grid(row=3, sticky="NE")
                ttk.Label(self, text=f.reason).grid(row=3, column=1, sticky="W")

                ttk.Label(self, text="Status:").grid(row=4, sticky="NE")
                ttk.Label(self, text=FinancialRequestStatus(f.status).name).grid(row=4, column=1, sticky="W")

                if f.status == FinancialRequestStatus.Pending.value:
                    b1 = ttk.Button(self, text="Approve",
                               command=lambda: self.ctrl.search_financial_request_decide(self, 2))
                    b1.grid(row=5, column=0)
                    b1 = ttk.Button(self, text="Reject",
                               command=lambda: self.ctrl.search_financial_request_decide(self, 3))
                    b1.grid(row=5, column=1)