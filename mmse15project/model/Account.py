from enum import Enum

class AccountType(Enum):
    customerServiceAccount              = 1,
    customerServiceOfficerAccount       = 2

class Account:
    def setName(self, name):
        self.name = name

    def setID(self, id):
        self.id = id

    def setAccountType(self, type):
        self.accountType = type

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def getAccountType(self):
        return self.accountType

