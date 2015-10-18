import sys
from mmse15project.views.Administration import Administration
from mmse15project.views.CustomerService import CustomerService
from mmse15project.views.Financial import Financial
from mmse15project.views.HR import HR
from mmse15project.views.Marketing import Marketing
from mmse15project.views.Production import Production
from mmse15project.views.Service import Service
from mmse15project.views.TopManagement import TopManagement
from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType
from mmse15project.model.Account import Account
from mmse15project.model.Client import Client
from mmse15project.model.Request import Request
from mmse15project.model.RequestDetails import RequestDetails

class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_frame(self, frame_class, account=None):
        self.clear_frame(self.view.container)  # clear container
        if account is None:
            frame = frame_class(self.view.container, self.model, self)
        else:
            frame = frame_class(self.view.container, self.model, self,
                                AccountType(account.getAccountType()).name,
                                account.getEmail())
        frame.pack()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def login_auth(self, login):
        account = self.model.account_db.login(login.e1.get()+"@sep.se", login.e2.get())
        if account is False:
            self.clear_frame(login)
            login.fail()
        else:
            team_name = AccountTeam(account.getAccountTeam()).name
            self.set_frame(getattr(sys.modules[__name__], team_name), account)

    def login_try_again(self, login):
        self.clear_frame(login)
        login.auth()

    def login_quit(self):
        sys.exit()

    # Submit forms

    def new_account_submit(self, form):
        data = form.get_all()
        data[1] += "@sep.se"
        data[3] = self.str_to_enum(data[3]).value
        data[4] = self.str_to_enum(data[4]).value
        print(data)
        new = Account()
        new.setName(data[0])
        new.setEmail(data[1])
        new.setPassword(data[2])
        new.setAccountTeam(data[3])
        new.setAccountType(data[4])
        new.setDepartment(data[5])
        new.setComment(data[6])
        print(new.getAll())
        self.model.account_db.add(new)

    def str_to_enum(self, str):
        if str == "Administration":
            return AccountTeam.Administration
        elif str == "HR":
            return AccountTeam.HR
        elif str == "Customer Service":
            return AccountTeam.CustomerService
        elif str == "Marketing":
            return AccountTeam.Marketing
        elif str == "Financial":
            return AccountTeam.Financial
        elif str == "Production":
            return AccountTeam.Production
        elif str == "Service":
            return AccountTeam.Service
        elif str == "Top Management":
            return AccountTeam.TopManagement
        elif str == "Employee":
            return AccountType.Employee
        elif str == "Senior":
            return AccountType.Senior
        elif str == "Manager":
            return AccountType.Manager
        else:
            print("error: MainController.str_to_enum()")

    def new_client_submit(self, form):
        data = form.get_all()
        print(data)
        new= Client()
        new.setName(data[0])
        new.setEmail(data[1])
        new.setAddress(data[2])
        new.setPostalCode(data[3])
        new.setCity(data[4])
        new.setBirthDate(data[5])
        print(new.getAll())
        self.model.client_db.add(new)

    def new_request_submit(self, form):
        data = form.get_all()
        print(data)
        new = Request()
        new.setClientID(data[0])
        new.setEventType(data[1])
        new.setStartDate(data[2])
        new.setEndDate(data[3])
        new.setExpectedParticipants(data[4])
        new.setPreferences(data[5])
        new.setExpectedBudget(data[6])
        print(new.getAll())
        self.model.request_db.add(new)

    def new_request_details_submit(self, form):
        data = form.get_all()
        print(data)
        new = RequestDetails()
        new.setAll(data)
        print(new.getAll())
        self.model.request_details_db.add(new)
