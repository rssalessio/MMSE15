from mmse15project.model.Account import AccountType
from mmse15project.views.Marketing import Marketing
from tests.views.FrameTests import FrameTests


class MarketingTests:
    def __init__(self):
        self.root = FrameTests(Marketing, AccountType(3).name, "name@test.com")

MarketingTests().root.mainloop()
