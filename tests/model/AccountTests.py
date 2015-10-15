from mmse15project.model.Account import  *
from mmse15project.model.Account import  *


def AccountTest():
    acc = Account()
    acc.setName("alessio russo")
    assert(acc.getName() == "alessio russo")
    acc.setEmail("test@kth.se")
    assert(acc.getEmail() == "test@kth.se")
