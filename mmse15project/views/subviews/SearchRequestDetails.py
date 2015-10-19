import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst
import tkinter as tk


class SearchRequestDetails(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")

        self.e2 = ttk.Entry(self)  # Email
        self.e2.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Search",
                        command=lambda: self.ctrl.search_request_details_search(self))
        b1.grid(row=1, columnspan=2)

        self.result = self.SearchResult(self, self.model, self.ctrl)
        self.result.grid(row=2, columnspan=2)

    def get_all(self):
        return [self.e1.get()]

    class SearchResult(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            request_details = self.model.request_details_db.getByID(self.master.e2.get())
            if request_details is False:
                ttk.Label(self, text="Request not found").grid(row=0, columnspan=2)
            else:
                data = request_details.getAll()

                ttk.Label(self, text="Decorations", font="-underline true").grid(row=0, column=0, sticky="W")
                ttk.Label(self, text=data[0]).grid(row=1, column=0, columnspan=2, sticky="NW")
                ttk.Label(self, text="Filming/Photos", font="-underline true").grid(row=2, column=0, sticky="W")
                ttk.Label(self, text=data[1]).grid(row=3, column=0, columnspan=2, sticky="NW")
                ttk.Label(self, text="Filming/Photos", font="-underline true").grid(row=4, column=0, sticky="W")
                ttk.Label(self, text=data[2]).grid(row=5, column=0, columnspan=2, sticky="NW")

                ttk.Label(self, text="Food/Drinks", font="-underline true").grid(row=0, column=2, sticky="W")
                ttk.Label(self, text=data[3]).grid(row=1, column=2, columnspan=2, sticky="NW")
                ttk.Label(self, text="Music", font="-underline true").grid(row=2, column=2, sticky="W")
                ttk.Label(self, text=data[4]).grid(row=3, column=2, columnspan=2, sticky="NW")
                ttk.Label(self, text="Computer-Related Issues", font="-underline true").grid(row=4, column=2, sticky="W")
                ttk.Label(self, text=data[5]).grid(row=5, column=2, columnspan=2, sticky="NW")

                ttk.Label(self, text="Other needs", font="-underline true").grid(row=6, column=0, sticky="W")
                ttk.Label(self, text=data[5]).grid(row=7, column=0, columnspan=4, sticky="NW")
