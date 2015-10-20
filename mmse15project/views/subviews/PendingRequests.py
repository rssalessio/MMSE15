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
        self.update.create_widgets()

    class Update(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            acc_team = self.master.master.master.acc_team
            if acc_team == "CustomerService":
                requests = self.model.request_db.getByStatus(1) + self.model.request_db.getByStatus(4)
            elif acc_team == "Financial":
                requests = self.model.request_db.getByStatus(2)
            elif acc_team == "Administration":
                requests = self.model.request_db.getByStatus(3)
            else:
                requests = []

            if len(requests) == 0:
                ttk.Label(self, text="No pending requests").grid()
                return

            ttk.Label(self, text="RequestID(Status):").grid(row=0, sticky="E")
            ttk.Label(self, text="Event type").grid(row=0, column=1, sticky="W")
            row = 1
            for r in requests:
                ttk.Label(self, text=str(r.getID()) + "(" + str(r.getStatus()) + "):").grid(row=row, sticky="E")
                ttk.Label(self, text=r.getEventType()).grid(row=row, column=1, sticky="W")
                row += 1
