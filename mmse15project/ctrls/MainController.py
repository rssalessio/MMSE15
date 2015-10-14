import sys

class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_frame(self, frame_class):
        self.clear_frame(self.view.container)  # clear container
        frame = frame_class(self.view.container, self.model, self)
        frame.pack()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def login_auth(self, login):
        print("user: %s, pass: %s" % (login.e1.get(), login.e2.get()))
        self.clear_frame(login)
        login.fail()

    def login_try_again(self, login):
        self.clear_frame(login)
        login.auth()

    def login_quit(self):
        sys.exit()
