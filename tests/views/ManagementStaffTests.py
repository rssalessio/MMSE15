from mmse15project.views.ManagementStaff import ManagementStaff
from tests.views.FrameTests import FrameTests


class ManagementStaffTests:
    def __init__(self):
        self.root = FrameTests(ManagementStaff)

ManagementStaffTests().root.mainloop()
