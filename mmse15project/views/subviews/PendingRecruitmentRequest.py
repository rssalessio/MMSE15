import tkinter.ttk as ttk
from mmse15project.model.Task import TaskStatus
from mmse15project.model.Task import TaskPriority


class PendingRecruitmentRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        b1 = ttk.Button(self, text="Update",
                       command=lambda:
                       self.ctrl.pending_recruitment_request_update(self))
        b1.grid(row=0)

        self.update = self.Update(self, self.model, self.ctrl)
        self.update.grid(row=1)
        self.update.create_widgets()

    class Update(ttk.Frame):
        def __init__(self, master, model, ctrl):
            ttk.Frame.__init__(self, master)
            self.master = master
            self.model = model
            self.ctrl = ctrl

        def create_widgets(self):
            self.ctrl.clear_frame(self)
            recruitments = self.model.recruitment_request_db.getByStatus(1)
            if len(recruitments) == 0:
                ttk.Label(self, text="No pending recruitments").grid()
                return
            ttk.Label(self, text="RecruitmentID:").grid(row=0, sticky="E")
            ttk.Label(self, text="Job title").grid(row=0, column=1, sticky="W")
            row = 1
            for r in recruitments:
                ttk.Label(self, text=str(r.id) + ":").grid(row=row, sticky="E")
                ttk.Label(self, text=r.title).grid(row=row, column=1, sticky="W")
                row += 1
