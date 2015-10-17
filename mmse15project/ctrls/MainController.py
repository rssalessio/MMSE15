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

class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

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

        if login.e1.get() == "Sysadmin":
            self.set_frame(Sysadmin)
        elif login.e1.get() == "Administration":
            self.set_frame(Administration, "[account type]", "[user]")
        elif login.e1.get() == "CustomerService":
            self.set_frame(CustomerService, "[account type]", "[user]")
        elif login.e1.get() == "Financial":
            self.set_frame(Financial, "[account type]", "[user]")
        elif login.e1.get() == "HR":
            self.set_frame(HR, "[account type]", "[user]")
        elif login.e1.get() == "Marketing":
            self.set_frame(Marketing, "[account type]", "[user]")
        elif login.e1.get() == "Production":
            self.set_frame(Production, "[account type]", "[user]")
        elif login.e1.get() == "Service":
            self.set_frame(Service, "[account type]", "[user]")
        elif login.e1.get() == "TopManagement":
            self.set_frame(TopManagement, "[account type]", "[user]")
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
