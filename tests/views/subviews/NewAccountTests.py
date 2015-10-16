from mmse15project.views.subviews.NewAccount import NewAccount
from tests.views.FrameTests import FrameTests


class NewAccountTests:
    def __init__(self):
        self.root = FrameTests(NewAccount)

NewAccountTests().root.mainloop()
