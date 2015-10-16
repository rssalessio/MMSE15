from enum import Enum

class AccountType(Enum):
    invalidType                         = 0,
    employee                            = 1,
    officer                             = 2,
    manager                             = 3,
    freelancer                          = 4,

class AccountTeam(Enum):
    invalidTeam                         = 0,
    administration                      = 1,
    hr                                  = 2,
    customerService                     = 3,
    marketing                           = 4,
    financial                           = 5,
    production                          = 6,
    service                             = 7,
    management                          = 8


class Account:
    def __init__(self,email="",password="",name="",atype= AccountType.invalidType,accountTeam = AccountTeam.invalidTeam, comment=''):
        self.password = password
        self.email = email
        self.name = name
        self.accountType = atype
        self.accountTeam = accountTeam
        self.comment = comment

    def setName(self, name):
        self.name = name

    def setPassword(self,password):
        self.password = password

    def setAccountType(self, type):
        self.accountType = type

    def setEmail(self, email):
        self.email = email

    def setAccountTeam(self, at):
        self.accountTeam = at

    def setComment(self,comment):
        self.comment = comment

    def setAllData(self,list):
        self.email = list[0]
        self.password = list[1]
        self.name = list[2]
        self.accountType = list[3]
        self.accountTeam = list[4]
        self.accountQualification = list[5]
        self.department = list[6]
        self.comment = list[7]

    def getName(self):
        return self.name

    def getAccountType(self):
        return self.accountType

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getDepartment(self):
        return self.department

    def getAccountTeam(self):
        return self.accountTeam

    def getAccountQualification(self):
        return self.accountQualification

    def getComment(self):
        return self.comment

    def getAllData(self):
        return (self.getEmail(), self.getPassword(), self.getName(), self.getAccountType(),
                  self.getAccountTeam(), self.getAccountQualification(), self.getDepartment(), self.getComment())
