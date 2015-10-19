import tkinter.ttk as ttk


class PendingRequests(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        b1 = ttk.Button(self, text="Update",
                       command=lambda: self.ctrl.pending_requests_update(self))
        b1.grid(row=0)

        self.update = self.Update(self, self.model, self.ctrl)
        self.update.grid(row=1)

    class Update(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            acc_team = self.master.master.master.master.acc_team
            #print(acc_team)
            if acc_team == "CustomerService":
                requests = self.model.request_db.getByStatus(1) + self.model.request_db.getByStatus(4)
            elif acc_team == "Financial":
                requests = self.model.request_db.getByStatus(2)
            elif acc_team == "Administration":
                requests = self.model.request_db.getByStatus(3)
            else:
                requests = []

            ttk.Label(self, text="[RequestID]: [Even type]").grid(row=0, sticky="W")
            row = 1
            for r in requests:
                ttk.Label(self, text=str(r.getID()) + ": " + r.getEventType()).grid(row=row, sticky="W")
                row += 1

