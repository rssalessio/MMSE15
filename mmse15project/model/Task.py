from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    Invalid         = 0
    Pending         = 1
    Accepted        = 2
    Completed       = 3
    Other           = 4

class TaskPriority(Enum):
    Invalid         = 0
    Low             = 1
    Medium          = 2
    High            = 3
    Immediate       = 4

class Task:

    def __init__(self,requestid=0,description='', operator='', priority=TaskPriority.Invalid.value, deadline='',status=TaskStatus.Pending.value,comment=''):
        self.requestID = requestid
        self.description = description
        self.operator = operator
        self.priority = priority
        self.deadline = deadline
        self.status = status
        self.comment = comment

    def setAll(self,values):
        self.requestID = values[0]
        self.description = values[1]
        self.operator = values[2]
        self.priority = values[3]
        self.deadline = values[4]
        self.status = values[5]
        self.comment = values[6]

    def getAll(self): return (self.requestID,self.description,self.operator,self.priority,self.deadline,self.status,self.comment)
