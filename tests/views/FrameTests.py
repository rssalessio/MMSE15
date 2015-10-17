import tkinter as tk
from tests.views.MainControllerStandin import MainControllerStandin


class FrameTests(tk.Tk):
    def __init__(self, frame_class, acc_type=None, user=None):
        tk.Tk.__init__(self)
        self.title("FrameTests")
        self.resizable(tk.FALSE, tk.FALSE)
        self.attributes("-topmost", True)

        if (acc_type is None) and (user is None):
            f = frame_class(self, model=None, ctrl=MainControllerStandin(None, None))
        else:
            f = frame_class(self, model=None, ctrl=MainControllerStandin(None, None),
                            acc_type=acc_type, user=user)
        f.pack()
