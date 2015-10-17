from mmse15project.views.subviews.NewEventRequest import NewEventRequest
from tests.views.FrameTests import FrameTests


class NewEventRequestTests:
    def __init__(self):
        self.root = FrameTests(NewEventRequest)

NewEventRequestTests().root.mainloop()
