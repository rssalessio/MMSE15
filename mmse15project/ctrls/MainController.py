import sys
from mmse15project.views.subviews.Sysadmin import Sysadmin
from mmse15project.views.Administration import Administration
from mmse15project.views.CustomerService import CustomerService
from mmse15project.views.Financial import Financial
from mmse15project.views.HR import HR
from mmse15project.views.Marketing import Marketing
from mmse15project.views.Production import Production
from mmse15project.views.Service import Service
from mmse15project.views.TopManagement import TopManagement
from mmse15project.model.AccountDBInterface import  *
from mmse15project.model.Account import *
class MainController:
    def __init__(self, model, view, database):
        self.model = model
        self.view = view
        self.database = database
        self.accountDB = AccountDBInterface(self.database)

    def set_frame(self, frame_class, acc_type=None, user=None):
        self.clear_frame(self.view.container)  # clear container
        if (acc_type is None) and (user is None):
            frame = frame_class(self.view.container, self.model, self)
        else:
            frame = frame_class(self.view.container, self.model, self, acc_type, user)
        frame.pack()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def login_auth(self, login):

        print(login.get_all())
        account = self.accountDB.login(login.e1.get()+"@sep.se", login.e2.get())
        if (account == False):
            self.clear_frame(login)
            login.fail()
        else:
            if account.getAccountTeam() == AccountTeam.administration.value[0]:
                self.set_frame(Administration, account.getAccountType(), account.getEmail())
            elif account.getAccountTeam() == AccountTeam.customerService.value[0]:
                self.set_frame(CustomerService, account.getAccountType(), account.getEmail())
            elif account.getAccountTeam() == AccountTeam.financial.value[0]:
                self.set_frame(Financial, account.getAccountType(), account.getEmail())
            elif account.getAccountTeam() == AccountTeam.marketing.value[0]:
                self.set_frame(Marketing, account.getAccountType(), account.getEmail())
            elif account.getAccountTeam() == AccountTeam.production.value[0]:
                self.set_frame(Production, account.getAccountType(), account.getEmail())
            elif account.getAccountTeam() == AccountTeam.hr.value[0]:
                self.set_frame(HR, account.getAccountType(), account.getEmail())
            elif account.getAccountTeam() == AccountTeam.service.value[0]:
                self.set_frame(Service, account.getAccountType(), account.getEmail())
            elif account.getAccountTeam() == AccountTeam.topManagement.value[0]:
                self.set_frame(TopManagement, account.getAccountType(), account.getEmail())
            else:
                self.clear_frame(login)
                login.fail()

    def login_try_again(self, login):
        self.clear_frame(login)
        login.auth()

    def login_quit(self):
        sys.exit()

    def submit(self, subview):
        print(subview.get_all())
