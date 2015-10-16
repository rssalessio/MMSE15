from mmse15project.views.TopManagement import TopManagement
from tests.views.FrameTests import FrameTests


class TopManagementTests:
    def __init__(self):
        self.root = FrameTests(TopManagement, "acc3", "usr5")

TopManagementTests().root.mainloop()
