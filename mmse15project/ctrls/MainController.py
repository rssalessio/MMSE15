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

    def submit(self, subview):
        print(subview.get_all())
