import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst


# Form for creating a new RequestDetails
class NewRequestDetails(ttk.Frame):
    def __init__(self, master, model, ctrl, id):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.id = id
        self.create_widgets()

    def create_widgets(self):

        self.e1 = tkst.ScrolledText(self, width=30, height=5)
        self.e2 = tkst.ScrolledText(self, width=30, height=5)
        self.e3 = tkst.ScrolledText(self, width=30, height=5)
        self.e4 = tkst.ScrolledText(self, width=30, height=5)
        self.e5 = tkst.ScrolledText(self, width=30, height=5)
        self.e6 = tkst.ScrolledText(self, width=30, height=5)
        self.e7 = tkst.ScrolledText(self, width=60, height=5)

        ttk.Label(self, text="Decorations", font="-underline true").grid(row=0, column=0, sticky="E")
        self.e1.grid(row=1, column=0, columnspan=2)
        ttk.Label(self, text="Filming/Photos", font="-underline true").grid(row=2, column=0, sticky="E")
        self.e2.grid(row=3, column=0, columnspan=2)
        ttk.Label(self, text="Filming/Photos", font="-underline true").grid(row=4, column=0, sticky="E")
        self.e3.grid(row=5, column=0, columnspan=2)

        ttk.Label(self, text="Food/Drinks", font="-underline true").grid(row=0, column=2, sticky="E")
        self.e4.grid(row=1, column=2, columnspan=2)
        ttk.Label(self, text="Music", font="-underline true").grid(row=2, column=2, sticky="E")
        self.e5.grid(row=3, column=2, columnspan=2)
        ttk.Label(self, text="Computer-Related Issues", font="-underline true").grid(row=4, column=2, sticky="E")
        self.e6.grid(row=5, column=2, columnspan=2)

        ttk.Label(self, text="Other needs", font="-underline true").grid(row=6, column=0, sticky="E")
        self.e7.grid(row=7, column=0, columnspan=4)

        b1 = ttk.Button(self, text="Submit",
                       command=lambda: self.ctrl.new_request_details_submit(self))
        b1.grid(columnspan=4)

    def get_all(self):
        return [self.id, self.e1.get(1.0, tk.END), self.e2.get(1.0, tk.END),
                self.e3.get(1.0, tk.END), self.e4.get(1.0, tk.END),
                self.e5.get(1.0, tk.END), self.e6.get(1.0, tk.END),
                self.e7.get(1.0, tk.END)]
