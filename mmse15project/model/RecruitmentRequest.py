from enum import Enum

class RecruitmentType(Enum):
    invalidType =0,
    outsource   =1,
    hire        =2

class RecruitmentStatus(Enum):
    invalidType =0,
    active = 1,
    completed = 2


class RecruitmentRequest:
    def __init__(self, id=0, type=RecruitmentType.invalidType, date='01/01/1991',department='',title='',status=RecruitmentStatus.invalidType, description=''):
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