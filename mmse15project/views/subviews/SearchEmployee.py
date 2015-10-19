import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tkst


# Form for searching employees
class SearchEmployee(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Employee name:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1, sticky="W")

       # b1 = ttk.Button(self, text="Create",
                       # command=lambda: pass)
       # b1.grid(row=1, columnspan=2)

        #self.form = self.Form(self, self.model, self.ctrl)
        #self.form.grid(row=2, columnspan=2)

    class Form(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)

        def get_all(self):
            return []
