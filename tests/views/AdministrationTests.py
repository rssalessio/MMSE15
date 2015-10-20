#!/usr/bin/env python3
from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType
from mmse15project.views.Administration import Administration
from tests.views.FrameTests import FrameTests


class AdministrationTests:
    def __init__(self):
        self.root = FrameTests(Administration, AccountTeam(1).name, AccountType(3).name, "a@sep.se")

AdministrationTests().root.mainloop()
