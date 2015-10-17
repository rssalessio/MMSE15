from mmse15project.views.subviews.NewClientRecord import NewClientRecord
from tests.views.FrameTests import FrameTests


class NewClientRecordTests:
    def __init__(self):
        self.root = FrameTests(NewClientRecord)

NewClientRecordTests().root.mainloop()
