import tkinter as tk
from mmse15project.model.Model import Model
from mmse15project.ctrls.MainController import MainController


class FrameTests(tk.Tk):
    def __init__(self, frame_class, acc_type=None, user=None):
        tk.Tk.__init__(self)
        self.title("FrameTests")
        self.resizable(tk.FALSE, tk.FALSE)
        self.attributes("-topmost", True)

        model = Model()
        ctrl = MainController(model, None)

        if (acc_type is None) and (user is None):
            f = frame_class(self, model, ctrl)
        else:
            f = frame_class(self, model, ctrl, acc_type, user)
        f.pack()
