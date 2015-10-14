from enum import Enum

class AccountType(Enum):
    invalidAccount                      = 0,
    customerServiceAccount              = 1,
    customerServiceOfficerAccount       = 2

class Account:
    def __init__(self,email="",password="",name="",type= AccountType.invalidAccount):
        self.password = password
        self.email = email
        self.name = name
        self.accountType = type

    def setName(self, name):
        self.name = name

    def setPassword(self,password):
        self.password = password

    def setAccountType(self, type):
        self.accountType = type

    def setEmail(self, email):
        self.email = email

    def getName(self):
        return self.name
    def getAccountType(self):
        return self.accountType

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password
