import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst


# Form for creating a new RequestDetails
class NewRequestDetails(ttk.Frame):
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
                        command=lambda: self.ctrl.new_request_details_create(self))
        b1.grid(row=1, columnspan=2)

        self.form = self.Form(self, self.model, self.ctrl)
        self.form.grid(row=2, columnspan=2)

    class Form(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.model = model
            self.ctrl = ctrl

        def no_request_found(self):
            self.ctrl.clear_frame(self)
            ttk.Label(self, text="No valid request found").grid()

        def create_widgets(self):
            self.ctrl.clear_frame(self)
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
            return [self.master.e1.get(), self.e1.get(1.0, tk.END)[:-1], self.e2.get(1.0, tk.END)[:-1],
                    self.e3.get(1.0, tk.END)[:-1], self.e4.get(1.0, tk.END)[:-1],
                    self.e5.get(1.0, tk.END)[:-1], self.e6.get(1.0, tk.END)[:-1],
                    self.e7.get(1.0, tk.END)[:-1]]

