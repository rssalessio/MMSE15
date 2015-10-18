import tkinter as tk
import tkinter.ttk as ttk


# Form for creating a new Request
class NewRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_form()

    def create_form(self):
        ttk.Label(self, text="ClientID:").grid(row=0, sticky=tk.E)
        ttk.Label(self, text="Client name:").grid(row=1, sticky=tk.E)
        ttk.Label(self, text="Event type:").grid(row=2, sticky=tk.E)
        ttk.Label(self, text="From:").grid(row=3, sticky=tk.E)
        ttk.Label(self, text="To:").grid(row=4, sticky=tk.E)
        ttk.Label(self, text="Attendees:").grid(row=5, sticky=tk.E)
        ttk.Label(self, text="Preferences", font="-underline true").grid(row=6, sticky=tk.E)
        ttk.Label(self, text="Expected budget:").grid(row=10, sticky=tk.E)

        self.e1 = ttk.Entry(self)  # ClientID
        self.e1.grid(row=0, column=1)
        self.e2 = ttk.Entry(self)  # Client name
        self.e2.grid(row=1, column=1)
        self.e3 = ttk.Entry(self)  # Event type
        self.e3.grid(row=2, column=1)
        self.e4 = ttk.Entry(self)  # From
        self.e4.grid(row=3, column=1)
        self.e5 = ttk.Entry(self)  # To
        self.e5.grid(row=4, column=1)
        self.e6 = ttk.Entry(self)  # Attendees
        self.e6.grid(row=5, column=1)

        # Preferences
        self.e7 = tk.IntVar(self)
        ttk.Checkbutton(self, text="Decorations", variable=self.e7).grid(row=7, sticky=tk.W)
        self.e8 = tk.IntVar(self)
        ttk.Checkbutton(self, text="Breakfast, lunch, dinner", variable=self.e8).grid(row=7, column=1, sticky=tk.W)
        self.e9 = tk.IntVar(self)
        ttk.Checkbutton(self, text="Parties", variable=self.e9).grid(row=8, sticky=tk.W)
        self.e10 = tk.IntVar(self)
        ttk.Checkbutton(self, text="Soft/hotdrinks", variable=self.e10).grid(row=8, column=1, sticky=tk.W)
        self.e11 = tk.IntVar(self)
        ttk.Checkbutton(self, text="Photos/filming", variable=self.e11).grid(row=9, sticky=tk.W)

        self.e12 = ttk.Entry(self) # Expected budget
        self.e12.grid(row=10, column=1)

        b1 = ttk.Button(self, text="Submit",
                       command=lambda: self.ctrl.submit(self))
        b1.grid(columnspan=2)

    def get_all(self):
        return [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),
                self.e5.get(), self.e6.get(), self.e7.get(), self.e8.get(),
                self.e9.get(), self.e10.get(), self.e11.get(), self.e12.get()]
