import tkinter.ttk as ttk


class SearchRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Search",
                        command=lambda: self.ctrl.search_request_search(self))
        b1.grid(row=1, columnspan=2)

        self.result = self.SearchResult(self, self.model, self.ctrl)
        self.result.grid(row=2, columnspan=2)

    class SearchResult(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            request = self.model.request_db.getByID(self.master.e1.get())
            self.request = request
            if request is False:
                ttk.Label(self, text="Request not found").grid(row=0, columnspan=2)
            else:
                client = self.model.client_db.getByID(request.getClientID())
                if client is None:
                    ttk.Label(self, text="Request is invalid").grid(row=0, columnspan=2)
                else:
                    #ttk.Label(self, text="ClientID:").grid(row=0, sticky="E")
                    #ttk.Label(self, text=str(request.getClientID())).grid(row=0, column=1, sticky="W")

                    email = self.model.client_db.getByID(request.getClientID()).getEmail()
                    ttk.Label(self, text="Client email:").grid(row=0, sticky="E")
                    ttk.Label(self, text=email).grid(row=0, column=1, sticky="W")

                    ttk.Label(self, text="Event type:").grid(row=1, sticky="E")
                    ttk.Label(self, text=request.getEventType()).grid(row=1, column=1, sticky="W")

                    ttk.Label(self, text="From:").grid(row=2, sticky="E")
                    ttk.Label(self, text=request.getStartDate()).grid(row=2, column=1, sticky="W")

                    ttk.Label(self, text="To:").grid(row=3, sticky="E")
                    ttk.Label(self, text=request.getEndDate()).grid(row=3, column=1, sticky="W")

                    ttk.Label(self, text="Attendees:").grid(row=4, sticky="E")
                    ttk.Label(self, text=request.getExpectedParticipants()).grid(row=4, column=1, sticky="W")

                    ttk.Label(self, text="Preferences:").grid(row=5, sticky="NE")
                    ttk.Label(self, text=request.getPreferences()).grid(row=5, column=1, sticky="W")

                    ttk.Label(self, text="Expected budget:").grid(row=6, sticky="E")
                    ttk.Label(self, text=request.getExpectedBudget()).grid(row=6, column=1, sticky="W")

                    ttk.Label(self, text="Status:").grid(row=7, sticky="E")
                    ttk.Label(self, text=str(request.getStatus())).grid(row=7, column=1, sticky="W")

                    status = request.getStatus()
                    acc_team = self.master.master.master.master.acc_team
                    acc_type = self.master.master.master.master.acc_type

                    if (status == 1 and acc_team == "CustomerService" and acc_type == "Senior") or\
                            (status == 2 and acc_team == "Financial" and acc_type == "Manager") or\
                            (status == 3 and acc_team == "Administration" and acc_type == "Manager") or\
                            (acc_team == "CustomerService" and acc_type == "Manager"):
                        b1 = ttk.Button(self, text="Approve",
                            command=lambda: self.ctrl.search_request_approve(self))
                        b1.grid(row=8, column=0)
                        b2 = ttk.Button(self, text="Reject",
                                        command=lambda: self.ctrl.search_request_reject(self))
                        b2.grid(row=8, column=1)




