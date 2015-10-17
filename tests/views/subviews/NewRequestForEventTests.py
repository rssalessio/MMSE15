from mmse15project.views.subviews.NewRequestForEvent import NewRequestForEvent
from tests.views.FrameTests import FrameTests


class NewRequestForEventTests:
    def __init__(self):
        self.root = FrameTests(NewRequestForEvent)

NewRequestForEventTests().root.mainloop()
