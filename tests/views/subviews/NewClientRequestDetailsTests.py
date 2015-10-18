from mmse15project.views.subviews.NewRequestDetails import NewClientRequestDetails
from tests.views.FrameTests import FrameTests


class NewClientRequestDetailsTests:
    def __init__(self):
        self.root = FrameTests(NewClientRequestDetails)

NewClientRequestDetailsTests().root.mainloop()
