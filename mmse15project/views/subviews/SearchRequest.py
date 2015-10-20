import tkinter.ttk as ttk
from mmse15project.model.Task import TaskStatus
from mmse15project.model.Task import TaskPriority
import tkinter as tk
import tkinter.scrolledtext as tkst

class SearchRequest(ttk.Frame):
    def __init__(self, master, model, ctrl):
        ttk.Frame.__init__(self, master)
        self.model = model
        self.ctrl = ctrl
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="RequestID:").grid(row=0, sticky="E")
        self.e1 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)

        b1 = ttk.Button(self, text="Get",
                        command=lambda: self.ctrl.search_request_get(self))
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
            request = self.model.request_db.getByID(self.master.e1.get())
            self.request = request
            if request is False:
                ttk.Label(self, text="No such request").grid(row=0, columnspan=2)
            else:
                client = self.model.client_db.getByID(request.getClientID())
                if client is None:
                    ttk.Label(self, text="Invalid request").grid(row=0, columnspan=2)
                else:
                    #ttk.Label(self, text="ClientID:").grid(row=0, sticky="E")
                    #ttk.Label(self, text=str(request.getClientID())).grid(row=0, column=1, sticky="W")

                    email = self.model.client_db.getByID(request.getClientID()).getEmail()
                    ttk.Label(self, text="Client email:").grid(row=0, sticky="E")
                    ttk.Label(self, text=email).grid(row=0, column=1, sticky="W")

                    ttk.Label(self, text="Event type:").grid(row=1, sticky="E")
                    ttk.Label(self, text=request.getEventType()).grid(row=1, column=1, sticky="W")

                    ttk.Label(self, text="From:").grid(row=2, sticky="E")
                    ttk.Label(self, text=request.getStartDate()).grid(row=2, column=1, sticky="W")

                    ttk.Label(self, text="To:").grid(row=3, sticky="E")
                    ttk.Label(self, text=request.getEndDate()).grid(row=3, column=1, sticky="W")

                    ttk.Label(self, text="Attendees:").grid(row=4, sticky="E")
                    ttk.Label(self, text=request.getExpectedParticipants()).grid(row=4, column=1, sticky="W")

                    ttk.Label(self, text="Preferences:").grid(row=5, sticky="NE")
                    ttk.Label(self, text=request.getPreferences()).grid(row=5, column=1, sticky="W")

                    ttk.Label(self, text="Expected budget:").grid(row=6, sticky="E")
                    ttk.Label(self, text=request.getExpectedBudget()).grid(row=6, column=1, sticky="W")

                    ttk.Label(self, text="Status:").grid(row=7, sticky="E")
                    ttk.Label(self, text=str(request.getStatus())).grid(row=7, column=1, sticky="W")
                    status = request.getStatus()
                    acc_team = self.master.master.master.acc_team
                    acc_type = self.master.master.master.acc_type

                    if (status == 1 and acc_team == "CustomerService" and acc_type == "Senior") or\
                            (status == 2 and acc_team == "Financial" and acc_type == "Manager") or\
                            (status == 3 and acc_team == "Administration" and acc_type == "Manager"):
                        ttk.Label(self, text="Comment:").grid(row=8, sticky="E")
                        self.e8 = tkst.ScrolledText(self, width=20, height=5)
                        self.e8.grid(row=8, column=1)
                        self.e8.insert(tk.INSERT,request.comment)
                    else:
                        ttk.Label(self, text="Comment:").grid(row=8, sticky="E")
                        ttk.Label(self, text=str(request.comment)).grid(row=8, column=1, sticky="W")



                    ttk.Label(self, text="").grid(row=9, columnspan=2, sticky="WE")

                    # View assigned tasks
                    row = 10
                    tasks = self.model.task_db.getByRequestID(request.getID())
                    if tasks is False:
                        ttk.Label(self, text="No assigned tasks found").grid(row=row, columnspan=2)
                        row += 1
                    else:
                        ttk.Label(self, text="TaskID(Priority):").grid(row=row, sticky="E")
                        ttk.Label(self, text="Status").grid(row=row, column=1, sticky="W")
                        row += 1
                        for t in tasks:
                            priority = TaskPriority(t.priority).name
                            ttk.Label(self, text=str(t.id) + "(" + priority + "):").grid(row=row, sticky="E")
                            status = TaskStatus(t.status).name
                            ttk.Label(self, text=status).grid(row=row, column=1, sticky="W")
                            row += 1

                    # Buttons



                    if (status == 1 and acc_team == "CustomerService" and acc_type == "Senior") or\
                            (status == 2 and acc_team == "Financial" and acc_type == "Manager") or\
                            (status == 3 and acc_team == "Administration" and acc_type == "Manager"):
                        b1 = ttk.Button(self, text="Approve",
                            command=lambda: self.ctrl.search_request_approve(self))
                        b1.grid(row=row, column=0)
                        b2 = ttk.Button(self, text="Reject",
                                        command=lambda: self.ctrl.search_request_reject(self))
                        b2.grid(row=row, column=1)




