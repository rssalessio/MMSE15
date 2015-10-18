from mmse15project.views.subviews.NewRequestDetails import NewRequestDetails
from tests.views.FrameTests import FrameTests


class NewRequestDetailsTests:
    def __init__(self):
        self.root = FrameTests(NewRequestDetails)

NewRequestDetailsTests().root.mainloop()
