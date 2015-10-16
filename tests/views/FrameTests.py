import tkinter as tk
from mmse15project.ctrls.MainController import MainController


class FrameTests(tk.Tk):
    def __init__(self, frame_class):
        tk.Tk.__init__(self)
        self.title("FrameTests")
        self.resizable(tk.FALSE, tk.FALSE)
        self.attributes("-topmost", True)

        f = frame_class(self, model=None, ctrl=MainController(None, None))
        f.pack()
