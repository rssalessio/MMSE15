from enum import Enum

class RecruitmentType(Enum):
    invalidType =0,
    outsource   =1,
    hire        =2

class RecruitmentStatus(Enum):
    invalidType =0,
    active = 1,
    completed = 2


class RequestDetails:
    def __init__(self, id=0, detail1='', detail2='', detail3='',detail4='',detail5='',detail6='', needs=''):
        self.id=id
        self.detail1=detail1
        self.detail2=detail2
        self.detail3=detail3
        self.detail4=detail4
        self.detail5=detail5
        self.detail6=detail6
        self.needs = needs
    
    def setAll(self,values):
        self.id=values[0]
        self.detail1=values[1]
        self.detail2=values[2]
        self.detail3=values[3]
        self.detail4=values[4]
        self.detail5=values[5]
        self.detail6=values[6]
        self.needs = values[7]
        
    def getAll(self):
        return (self.id, self.detail1,self.detail2,self.detail3,self.detail4,self.detail5,self.detail6)


