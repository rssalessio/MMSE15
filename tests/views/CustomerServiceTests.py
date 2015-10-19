from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType
from mmse15project.views.CustomerService import CustomerService
from tests.views.FrameTests import FrameTests


class CustomerServiceTests:
    def __init__(self):
        self.root = FrameTests(CustomerService, AccountTeam(3).name, AccountType(2).name, "name@test.com")

CustomerServiceTests().root.mainloop()
