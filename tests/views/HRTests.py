from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType
from mmse15project.views.HR import HR
from tests.views.FrameTests import FrameTests


class HRTests:
    def __init__(self):
        self.root = FrameTests(HR, AccountTeam(2).name, AccountType(3).name, "name@test.com")

HRTests().root.mainloop()
