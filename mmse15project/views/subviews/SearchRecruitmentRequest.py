import tkinter.ttk as ttk
from mmse15project.model.RecruitmentRequest import RecruitmentStatus


class SearchRecruitmentRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="RecruitmentID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Get",
                        command=lambda: self.ctrl.search_recruitment_request_get(self))
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
            r = self.model.recruitment_request_db.getByID(wanted)
            self.r = r

            if r is False:
                ttk.Label(self, text="No such recruitment request").grid(row=0, columnspan=2)
            else:
                ttk.Label(self, text="Contract type:").grid(row=0, sticky="E")
                ttk.Label(self, text="Requesting department:").grid(row=1, sticky="E")
                ttk.Label(self, text="Job title:").grid(row=2, sticky="E")
                ttk.Label(self, text="Job description:").grid(row=3, sticky="NE")
                ttk.Label(self, text="Status:").grid(row=4, sticky="E")

                ttk.Label(self, text=r.date).grid(row=0, column=1, sticky="W")
                ttk.Label(self, text=r.department).grid(row=1, column=1, sticky="W")
                ttk.Label(self, text=r.title).grid(row=2, column=1, sticky="W")
                ttk.Label(self, text=r.description).grid(row=3, column=1, sticky="W")
                ttk.Label(self, text=RecruitmentStatus(r.status).name).grid(row=4, column=1, sticky="W")

                if r.status == RecruitmentStatus.Active.value:
                    b1 = ttk.Button(self, text="Completed",
                                    command=lambda: self.ctrl.search_recruitment_request_approve(self))
                    b1.grid(row=5, columnspan=2)




