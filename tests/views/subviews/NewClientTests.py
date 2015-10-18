from mmse15project.views.subviews.NewClient import NewClient
from tests.views.FrameTests import FrameTests


class NewClientTests:
    def __init__(self):
        self.root = FrameTests(NewClient)

NewClientTests().root.mainloop()
