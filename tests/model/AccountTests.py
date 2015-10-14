from mmse15project.model.Account import  *
from mmse15project.model.Account import  *


def AccountTest():
    acc = Account()
    acc.setName("alessio russo")
    assert(acc.getName() == "alessio russo")
    acc.setAccountType(AccountType.customerServiceAccount)
    assert(acc.getAccountType() ==  AccountType.customerServiceAccount)
    acc.setEmail("test@kth.se")
    assert(acc.getEmail() == "test@kth.se")
