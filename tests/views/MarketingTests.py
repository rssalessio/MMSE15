#!/usr/bin/env python3
from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType
from mmse15project.views.Marketing import Marketing
from tests.views.FrameTests import FrameTests


class MarketingTests:
    def __init__(self):
        self.root = FrameTests(Marketing, AccountTeam(4).name, AccountType(3).name, "m@sep.se")

MarketingTests().root.mainloop()
