from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType
from mmse15project.views.Production import Production
from tests.views.FrameTests import FrameTests


class ProductionTests:
    def __init__(self):
        self.root = FrameTests(Production, AccountTeam(6).name, AccountType(3).name, "name@test.com")

ProductionTests().root.mainloop()
