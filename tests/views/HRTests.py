from mmse15project.model.Account import AccountType
from mmse15project.views.HR import HR
from tests.views.FrameTests import FrameTests


class HRTests:
    def __init__(self):
        self.root = FrameTests(HR, AccountType(3).name, "name@test.com")

HRTests().root.mainloop()
