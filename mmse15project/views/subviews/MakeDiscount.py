import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tkst


# Form for making a discount
class MakeDiscount(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1, sticky="W")

        b1 = ttk.Button(self, text="Create",
                        command=lambda:self.form.create_widgets())
        b1.grid(row=1, columnspan=2)

        self.form = self.Form(self, self.model, self.ctrl)
        self.form.grid(row=2, columnspan=2)

    class Form(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
            ttk.Label(self, text="Amount:").grid(row=1, sticky="E")
            ttk.Label(self, text="Comment:").grid(row=2, sticky="E")
            ttk.Label(self, text="Date:").grid(row=3, sticky="E")

            self.e1 = self.master.e1.get()  # RequestID
            ttk.Label(self, text=self.e1).grid(row=0, column=1, sticky="W")
            self.e2 = ttk.Entry(self)  #Amount
            self.e2.grid(row=1, column=1)
            self.e3 = ttk.Entry(self)  # Comment
            self.e3.grid(row=2, column=1)
            self.e4 = ttk.Entry(self)  # Date
            self.e4.grid(row=3, column=1)


            b1 = ttk.Button(self, text="Submit",
                           command=lambda: self.ctrl.new_discount(self))
            b1.grid(columnspan=2)

        def get_all(self):
            return [self.e1, self.e2.get(), self.e3.get(), self.e4.get()]
