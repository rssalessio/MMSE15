from enum import Enum

class RecruitmentType(Enum):
    InvalidType =0
    Outsource   =1,
    Hire        =2

class RecruitmentStatus(Enum):
    InvalidType = 0
    Pending     = 1
    Accepted    = 2
    Rejected    = 3


class RecruitmentRequest:
    def __init__(self, id=0, type=RecruitmentType.InvalidType.value, date='01/01/1991',department='',title='',status=RecruitmentStatus.Pending.value, description=''):
        self.id=id
        self.type = type
        self.date = date
        self.department = department
        self.title = title
        self.status = status
        self.description = description
    
    def setAll(self,values):
        self.id=values[0]
        self.type = values[1]
        self.date = values[2]
        self.department = values[3]
        self.title = values[4]
        self.status = values[5]
        self.description = values[6]
        
    def getAll(self):
        return (self.id, self.type, self.date, self.department,self.title, self.status, self.description)