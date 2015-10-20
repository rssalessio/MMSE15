import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tkst


class SearchDiscount(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1, sticky="W")

        b1 = ttk.Button(self, text="Get",
                        command=lambda:self.ctrl.search_discount_get(self))
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

            if self.model.request_db.getByID(int(self.master.e1.get())) is False:
                ttk.Label(self, text="No such RequestID").grid()
                return
            discount = self.model.discount_db.getByRequestID(int(self.master.e1.get()))
            if discount is False:
                ttk.Label(self, text="No such discount").grid()
                return


            ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
            ttk.Label(self, text="Amount:").grid(row=1, sticky="E")
            ttk.Label(self, text="Comment:").grid(row=2, sticky="E")
            ttk.Label(self, text="Date (MM/DD/YYYY):").grid(row=3, sticky="E")

            ttk.Label(self, text=str(discount.requestID)).grid(row=0, column=1, sticky="W")
            ttk.Label(self, text=str(discount.amount)).grid(row=1, column=1)
            ttk.Label(self, text=discount.comment).grid(row=2, column=1)
            ttk.Label(self, text=discount.date).grid(row=3, column=1)

        def get_all(self):
            return [self.e1, self.e2.get(), self.e3.get(), self.e4.get()]
