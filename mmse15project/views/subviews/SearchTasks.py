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
        ttk.Label(self, text="Task#:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Show",
                        command=lambda: self.ctrl.search_tasks_search(self))
        b1.grid(row=1, columnspan=2)

        self.user = self.master.master.master.user
        self.result = self.SearchResult(self, self.model, self.ctrl)
        self.result.grid(row=2, columnspan=2)

    class SearchResult(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def not_found(self):
            self.ctrl.clear_frame(self)
            ttk.Label(self, text="No such task").grid(row=0, columnspan=2)

        def create_widgets(self, task):
            self.ctrl.clear_frame(self)
            self.task = task

            ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
            ttk.Label(self, text=str(task.requestID)).grid(row=0, column=1, sticky="W")

            ttk.Label(self, text="Description:").grid(row=1, sticky="NE")
            ttk.Label(self, text=task.description).grid(row=1, column=1, sticky="W")

            ttk.Label(self, text="Operator:").grid(row=2, sticky="E")
            ttk.Label(self, text=task.operator).grid(row=2, column=1, sticky="W")

            ttk.Label(self, text="Priority:").grid(row=3, sticky="E")
            print(task.priority)
            ttk.Label(self, text=TaskPriority(task.priority).name).grid(row=3, column=1, sticky="W")

            ttk.Label(self, text="Status:").grid(row=4, sticky="E")
            status = task.status
            ttk.Label(self, text=TaskStatus(status).name).grid(row=4, column=1, sticky="W")

            if TaskStatus.Pending.value == status:
                b1_text = "Accept"
            elif TaskStatus.Accepted.value == status:
                b1_text = "Completed"

            b1 = ttk.Button(self, text=b1_text,
                        command=lambda: self.ctrl.search_tasks_approve(self))
            b1.grid(columnspan=2)