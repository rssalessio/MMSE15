from mmse15project.views.subviews.NewRequest import NewRequest
from tests.views.FrameTests import FrameTests


class NewRequestTests:
    def __init__(self):
        self.root = FrameTests(NewRequest)

NewRequestTests().root.mainloop()
