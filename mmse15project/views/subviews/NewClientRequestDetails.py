import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst


# Form for creating a new Client Request Details
class NewClientRequestDetails(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_form()

    def create_form(self):
        self.line_entries()
        self.text_boxes()

        b1 = ttk.Button(self, text="Submit",
                       command=lambda: self.ctrl.submit(self))
        b1.grid(columnspan=4)

    def line_entries(self):
        ttk.Label(self, text="ClientID:").grid(row=0, sticky=tk.E)
        ttk.Label(self, text="Client name:").grid(row=1, sticky=tk.E)
        ttk.Label(self, text="Event type:").grid(row=2, sticky=tk.E)
        ttk.Label(self, text="Description:").grid(row=3, sticky=tk.E)
        ttk.Label(self, text="From:").grid(row=4, sticky=tk.E)

        self.e1 = ttk.Entry(self)  # ClientID
        self.e1.grid(row=0, column=1)
        self.e2 = ttk.Entry(self)  # Client name
        self.e2.grid(row=1, column=1)
        self.e3 = ttk.Entry(self)  # Event type
        self.e3.grid(row=2, column=1)
        self.e4 = ttk.Entry(self)  # Description
        self.e4.grid(row=3, column=1)
        self.e5 = ttk.Entry(self)  # From
        self.e5.grid(row=4, column=1)

        ttk.Label(self, text="Attendees:").grid(row=1, column=2, sticky=tk.E)
        ttk.Label(self, text="Planned budget:").grid(row=2, column=2, sticky=tk.E)
        ttk.Label(self, text="To:").grid(row=4, column=2, sticky=tk.E)

        self.e6 = ttk.Entry(self)  # Attendees
        self.e6.grid(row=1, column=3)
        self.e6 = ttk.Entry(self)  # Planned budget
        self.e6.grid(row=2, column=3)
        self.e6 = ttk.Entry(self)  # To
        self.e6.grid(row=4, column=3)

    def text_boxes(self):
        print("t_b")
        editArea = tkst.ScrolledText(
            master = self,
            wrap   = tk.WORD,
            width  = 20,
            height = 10
        )
        editArea.grid(row=5, columnspan=2)

    def get_all(self):
        return [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),
                self.e5.get(), self.e6.get(), self.e7.get(), self.e8.get(),
                self.e9.get(), self.e10.get(), self.e11.get(), self.e12.get()]
