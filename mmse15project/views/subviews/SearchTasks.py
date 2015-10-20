import tkinter.ttk as ttk
from mmse15project.model.Task import TaskPriority
from mmse15project.model.Task import TaskStatus


class SearchTasks(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="TaskID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Get",
                        command=lambda: self.ctrl.search_tasks_get(self))
        b1.grid(row=1, columnspan=2)

        self.result = self.Result(self, self.model, self.ctrl)
        self.result.grid(row=2, columnspan=2)

    class Result(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)

            wanted = int(self.master.e1.get())
            t = self.model.task_db.getByID(wanted)
            self.t = t

            if t is False:
                ttk.Label(self, text="No such task").grid(row=0, columnspan=2)
                return

            ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
            ttk.Label(self, text=str(t.requestID)).grid(row=0, column=1, sticky="W")

            ttk.Label(self, text="Description:").grid(row=1, sticky="NE")
            ttk.Label(self, text=t.description).grid(row=1, column=1, sticky="W")

            ttk.Label(self, text="Operator:").grid(row=2, sticky="E")
            ttk.Label(self, text=t.operator).grid(row=2, column=1, sticky="W")

            ttk.Label(self, text="Priority:").grid(row=3, sticky="E")
            ttk.Label(self, text=TaskPriority(t.priority).name).grid(row=3, column=1, sticky="W")

            ttk.Label(self, text="Status:").grid(row=4, sticky="E")
            ttk.Label(self, text=TaskStatus(t.status).name).grid(row=4, column=1, sticky="W")

            acc_type = self.master.master.master.acc_type
            user = self.master.master.master.user

            if t.status == TaskStatus.Pending.value and t.operator == user:
                b1_text = "Accept"
            elif t.status == TaskStatus.Accepted.value and t.operator == user:
                b1_text = "Request close"
            elif t.status == TaskStatus.Completed.value and acc_type == "Manager":
                b1_text = "Close"
            else:
                return

            b1 = ttk.Button(self, text=b1_text,
                        command=lambda: self.ctrl.search_tasks_approve(self))
            b1.grid(columnspan=2)
