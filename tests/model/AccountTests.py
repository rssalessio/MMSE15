from mmse15project.model.Account import  *

__author__ = ('tobias','alessior@kth.se')


def AccountTest():
    acc = Account()
    acc.setName("alessio russo")
    assert(acc.getName() == "alessio russo")
    acc.setID(911103192)
    assert(acc.getID() == 911103192)
    acc.setAccountType(AccountType.customerServiceAccount)
    assert(acc.getAccountType() ==  AccountType.customerServiceAccount)
