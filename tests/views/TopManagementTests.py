from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType
from mmse15project.views.TopManagement import TopManagement
from tests.views.FrameTests import FrameTests


class TopManagementTests:
    def __init__(self):
        self.root = FrameTests(TopManagement, AccountTeam(8).name, AccountType(3).name, "tm@sep.se")

TopManagementTests().root.mainloop()
