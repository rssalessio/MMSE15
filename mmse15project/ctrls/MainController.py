import sys

__author__ = 'tobias'


class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_frame(self, class_):
        self.clear_frame(self.view.container)
        class_(self, self.view.container)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def login_auth(self, login, username, password):
        print("%s:%s" % (username, password))
        self.clear_frame(login)
        login.fail()

    def login_try_again(self, login):
        self.clear_frame(login)
        login.auth()

    def login_quit(self):
        sys.exit()
