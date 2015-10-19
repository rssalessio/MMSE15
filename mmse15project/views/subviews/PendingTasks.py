import tkinter.ttk as ttk
from mmse15project.model.Task import TaskStatus
from mmse15project.model.Task import TaskPriority

class PendingTasks(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        b1 = ttk.Button(self, text="Update",
                       command=lambda: self.ctrl.pending_tasks_update(self))
        b1.grid(row=0)

        self.update = self.Update(self, self.model, self.ctrl)
        self.update.grid(row=1)

    class Update(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            user = self.master.master.master.master.user
            acc_type = self.master.master.master.master.acc_type

            print(acc_type)
            if acc_type == "Manager":
                tasks = self.model.task_db.getByStatus(3)
            else:
                tasks = self.model.task_db.getByStatusAndEmail(1, user) +\
                        self.model.task_db.getByStatusAndEmail(2, user)

            ttk.Label(self, text="Task#(Priority):").grid(row=0, sticky="E")
            ttk.Label(self, text="Status").grid(row=0, column=1, sticky="W")
            row = 1
            for t in tasks:
                priority = TaskPriority(t.priority).name
                ttk.Label(self, text=str(row) + "(" + priority + "):").grid(row=row, sticky="E")
                status = TaskStatus(t.status).name
                ttk.Label(self, text=status).grid(row=row, column=1, sticky="W")
                row += 1
