from enum import Enum


class AccountType(Enum):
    InvalidType                         = 0
    Employee                            = 1
    Senior                              = 2
    Manager                             = 3
    Freelancer                          = 4


class AccountTeam(Enum):
    InvalidTeam                         = 0
    Administration                      = 1
    HR                                  = 2
    CustomerService                     = 3
    Marketing                           = 4
    Financial                           = 5
    Production                          = 6
    Service                             = 7
    TopManagement                       = 8


class AccountQualification(Enum):
    InvalidQualification                = 0
    Generic                             = 1
    Photographer                        = 2
    Audio                               = 3
    Graphic                             = 4
    Decoration                          = 5
    Technical                           = 6
    Chef                                = 7
    Waitress                            = 8




class Account:
    def __init__(self,email="",password="",name="",atype= AccountType.InvalidType,accountTeam = AccountTeam.InvalidTeam, accountQualification= AccountQualification.InvalidQualification,department='', comment=''):
        self.password = password
        self.email = email
        self.name = name
        self.accountType = atype
        self.accountTeam = accountTeam
        self.accountQualification = accountQualification
        self.department = department
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

    def setAccountQualification(self,aq):
        self.accountQualification =aq

    def setDepartment(self,dep):
        self.department = dep

    def setComment(self,comment):
        self.comment = comment

    def setAll(self,list):
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

    def getAll(self):
        return (self.getEmail(), self.getPassword(), self.getName(), self.getAccountType(),
                  self.getAccountTeam(), self.getAccountQualification(), self.getDepartment(), self.getComment())
