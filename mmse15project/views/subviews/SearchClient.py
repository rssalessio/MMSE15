import tkinter.ttk as ttk


class SearchClient(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Email:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Search",
                       command=lambda: self.ctrl.search_client_search(self))
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
            client = self.model.client_db.getByEmail(self.master.e1.get())
            if client is False:
                ttk.Label(self, text="No result").grid(row=0, columnspan=2)
            else:
                ttk.Label(self, text="ClientID:").grid(row=0, sticky="E")
                ttk.Label(self, text=str(client.getID())).grid(row=0, column=1, sticky="W")

                ttk.Label(self, text="Full name:").grid(row=1, sticky="E")
                ttk.Label(self, text=client.getName()).grid(row=1, column=1, sticky="W")

                ttk.Label(self, text="Email:").grid(row=2, sticky="E")
                ttk.Label(self, text=client.getEmail()).grid(row=2, column=1, sticky="W")

                ttk.Label(self, text="Address:").grid(row=3, sticky="E")
                ttk.Label(self, text=client.getAddress()).grid(row=3, column=1, sticky="W")

                ttk.Label(self, text="Postal code:").grid(row=4, sticky="E")
                ttk.Label(self, text=client.getPostalCode()).grid(row=4, column=1, sticky="W")

                ttk.Label(self, text="City:").grid(row=5, sticky="E")
                ttk.Label(self, text=client.getCity()).grid(row=5, column=1, sticky="W")

                ttk.Label(self, text="Day of birth:").grid(row=6, sticky="E")
                ttk.Label(self, text=client.getBirthDate()).grid(row=6, column=1, sticky="W")

                ttk.Label(self, text="").grid(row=7, columnspan=2, sticky="WE")

                requests = self.model.request_db.getByClientID(client.getID())
                if requests is False:
                    ttk.Label(self, text="No requests found").grid(row=8, columnspan=2)
                else:
                    ttk.Label(self, text="RequestID(Status):").grid(row=8, sticky="E")
                    ttk.Label(self, text="Event type").grid(row=8, column=1, sticky="W")
                    row = 9
                    for r in requests:
                        ttk.Label(self, text=str(r.getID()) + "(" + str(r.getStatus()) + "):").grid(row=row, sticky="E")
                        ttk.Label(self, text=r.getEventType()).grid(row=row, column=1, sticky="W")
                        row += 1

