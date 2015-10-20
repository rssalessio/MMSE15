import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tkst


# Form for creating a new FinancialRequest
class NewFinancialRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1, sticky="W")

        b1 = ttk.Button(self, text="Create request",
                        command=lambda: self.ctrl.new_financial_request_create(self))
        b1.grid(row=1, columnspan=2)

        self.form = self.Form(self, self.model, self.ctrl)
        self.form.grid(row=2, columnspan=2)

    class Form(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.model = model
            self.ctrl = ctrl

        def not_found(self):
            self.ctrl.clear_frame(self)
            ttk.Label(self, text="No such RequestID (project reference)").grid()

        def create_widgets(self):
            self.ctrl.clear_frame(self)

            ttk.Label(self, text="Requesting department:").grid(row=0, sticky="E")
            self.e1 = ttk.Entry(self)
            self.e1.grid(row=0, column=1)

            ttk.Label(self, text="RequestID:").grid(row=1, sticky="E")
            self.e2 = self.master.e1.get()
            ttk.Label(self, text=str(self.e2)).grid(row=1, column=1, sticky="W")

            ttk.Label(self, text="Required amount:").grid(row=2, sticky="E")
            self.e3 = ttk.Entry(self)
            self.e3.grid(row=2, column=1)

            ttk.Label(self, text="Reason:").grid(row=3, sticky="NE")
            self.e4 = tkst.ScrolledText(self, width=20, height=5)
            self.e4.grid(row=3, column=1)

            b1 = ttk.Button(self, text="Submit",
                           command=lambda: self.ctrl.new_financial_request_submit(self))
            b1.grid(columnspan=2)

        def get_all(self):
            return [self.e1.get(), self.e2, self.e3.get(), self.e4.get(1.0, tk.END)[:-1]]
