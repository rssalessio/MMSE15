import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tkst


# Form for creating a new RecruitmentRequest
class NewRecruitmentRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        self.ctrl.clear_frame(self)
        ttk.Label(self, text="Contract type:").grid(row=0, sticky="E")
        ttk.Label(self, text="Requesting department:").grid(row=1, sticky="E")
        ttk.Label(self, text="Job title:").grid(row=2, sticky="E")
        ttk.Label(self, text="Job description:").grid(row=3, sticky="NE")

        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1, sticky="W")
        self.e2 = ttk.Entry(self)
        self.e2.grid(row=1, column=1, sticky="W")
        self.e3 = ttk.Entry(self)
        self.e3.grid(row=2, column=1, sticky="W")
        self.e4 = tkst.ScrolledText(self, width=20, height=5)
        self.e4.grid(row=3, column=1)

        b1 = ttk.Button(self, text="Request",
                        command=lambda: self.ctrl.new_recruitment_requests_submit(self))
        b1.grid(row=4, columnspan=2)

    def get_all(self):
            return [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(1.0, tk.END)[:-1]]
