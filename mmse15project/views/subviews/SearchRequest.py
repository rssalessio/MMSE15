import tkinter as tk
import tkinter.ttk as ttk


class SearchRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_form()

    def create_form(self):
        ttk.Label(self, text="ClientID:").grid(row=0, sticky=tk.E)

        self.e1 = ttk.Entry(self)  # ClientID
        self.e1.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Search",
                       command=lambda: self.ctrl.submit(self))
        b1.grid(row=1, columnspan=2)

        self.result = self.SearchResult(self, self.model, self.ctrl)
        self.result.grid(row=3, columnspan=2)

    def get_all(self):
        return [self.e1.get()]

    class SearchResult(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.model = model
            self.ctrl = ctrl
            self.create_widgets()

        def create_widgets(self):
            ttk.Label(self, text="[result]").grid(row=0, sticky=tk.E)
