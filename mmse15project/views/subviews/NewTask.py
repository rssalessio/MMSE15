import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tkst


# Form for creating a new Task
class NewTask(ttk.Frame):
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
                        command=lambda: self.ctrl.new_task_create(self))
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
            ttk.Label(self, text="RequestID not found!").grid()

        def create_widgets(self):
            self.ctrl.clear_frame(self)

            ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
            self.e1 = self.master.e1.get()
            ttk.Label(self, text=self.e1).grid(row=0, column=1, sticky="W")

            ttk.Label(self, text="Description:").grid(row=1, sticky="NE")
            self.e2 = tkst.ScrolledText(self, width=20, height=5)
            self.e2.grid(row=1, column=1, columnspan=2)

            ttk.Label(self, text="Operator:").grid(row=2, sticky="E")
            self.e3 = ttk.Entry(self)
            self.e3.grid(row=2, column=1)

            ttk.Label(self, text="Priority:").grid(row=3, sticky="E")
            priorities=[1, 2, 3]
            self.e4 = tk.IntVar(self)
            self.e4.set(priorities[0])
            ttk.OptionMenu(self, self.e4, self.e4.get(), *priorities).grid(row=3, column=1, sticky="E")

            b1 = ttk.Button(self, text="Submit",
                           command=lambda: self.ctrl.new_task_submit(self))
            b1.grid(columnspan=2)

        def get_all(self):
            return [self.e1, self.e2.get(1.0, tk.END)[:-1], self.e3.get(), self.e4.get()]
