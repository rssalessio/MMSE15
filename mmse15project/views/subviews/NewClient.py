import tkinter.ttk as ttk


# Form for creating a new Client
class NewClient(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_form()

    def create_form(self):
        ttk.Label(self, text="Full name:").grid(row=0, sticky="E")
        ttk.Label(self, text="Email:").grid(row=1, sticky="E")
        ttk.Label(self, text="Address:").grid(row=2, sticky="E")
        ttk.Label(self, text="Postal code:").grid(row=3, sticky="E")
        ttk.Label(self, text="City:").grid(row=4, sticky="E")
        ttk.Label(self, text="Day of birth:").grid(row=5, sticky="E")

        self.e1 = ttk.Entry(self)  # Full name
        self.e1.grid(row=0, column=1)
        self.e2 = ttk.Entry(self)  # Email
        self.e2.grid(row=1, column=1)
        self.e3 = ttk.Entry(self)  # Address
        self.e3.grid(row=2, column=1)
        self.e4 = ttk.Entry(self)  # Postal code
        self.e4.grid(row=3, column=1)
        self.e5 = ttk.Entry(self)  # City
        self.e5.grid(row=4, column=1)
        self.e6 = ttk.Entry(self)  # Day of birth
        self.e6.grid(row=5, column=1)

        b1 = ttk.Button(self, text="Submit",
                       command=lambda: self.ctrl.submit(self))
        b1.grid(columnspan=2)

    def get_all(self):
        return [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),
                self.e5.get(), self.e6.get()]
