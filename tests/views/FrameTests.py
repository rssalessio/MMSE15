import tkinter as tk
from mmse15project.model.Model import Model
from mmse15project.ctrls.MainController import MainController


class FrameTests(tk.Tk):
    def __init__(self, frame_class, acc_team, acc_type, user):
        tk.Tk.__init__(self)
        self.title("FrameTests")
        self.resizable(tk.FALSE, tk.FALSE)
        self.attributes("-topmost", True)

        model = Model()
        ctrl = MainController(model, None)

        frame_class(self, model, ctrl, acc_team, acc_type, user).pack()

