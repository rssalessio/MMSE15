#!/usr/bin/env python3
from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType
from mmse15project.views.CustomerService import CustomerService
from tests.views.FrameTests import FrameTests


class CustomerServiceTests:
    def __init__(self):
        self.root = FrameTests(CustomerService, AccountTeam(3).name, AccountType(1).name, "cs@sep.se")

CustomerServiceTests().root.mainloop()
