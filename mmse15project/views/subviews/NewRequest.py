import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tkst


# Form for creating a new Request
class NewRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="ClientID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1, sticky="W")

        b1 = ttk.Button(self, text="Create",
                        command=lambda: self.ctrl.new_request_create(self))
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
            ttk.Label(self, text="ClientID not found!").grid()


        def create_widgets(self):
            self.ctrl.clear_frame(self)
            ttk.Label(self, text="ClientID:").grid(row=0, sticky="E")
            ttk.Label(self, text="Event type:").grid(row=1, sticky="E")
            ttk.Label(self, text="From:").grid(row=2, sticky="E")
            ttk.Label(self, text="To:").grid(row=3, sticky="E")
            ttk.Label(self, text="Attendees:").grid(row=4, sticky="E")

            self.e1 = self.master.e1.get()  # ClientID
            ttk.Label(self, text=self.e1).grid(row=0, column=1, sticky="W")
            self.e2 = ttk.Entry(self)  # Event type
            self.e2.grid(row=1, column=1)
            self.e3 = ttk.Entry(self)  # From
            self.e3.grid(row=2, column=1)
            self.e4 = ttk.Entry(self)  # To
            self.e4.grid(row=3, column=1)
            self.e5 = ttk.Entry(self)  # Attendees
            self.e5.grid(row=4, column=1)

            # Preferences
            ttk.Label(self, text="Preferences:").grid(row=5, sticky="NE")
            self.e6 = tkst.ScrolledText(self, width=20, height=5)
            self.e6.grid(row=5, column=1, columnspan=2)

             # Expected budget
            ttk.Label(self, text="Expected budget:").grid(row=6, sticky="E")
            self.e7 = ttk.Entry(self)
            self.e7.grid(row=6, column=1)

            b1 = ttk.Button(self, text="Submit",
                           command=lambda: self.ctrl.new_request_submit(self))
            b1.grid(columnspan=2)

        def get_all(self):
            return [self.e1, self.e2.get(), self.e3.get(), self.e4.get(),
                    self.e5.get(), self.e6.get(1.0, tk.END)[:-1], self.e7.get()]
