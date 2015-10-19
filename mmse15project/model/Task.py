from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    Invalid         = 0
    Pending         = 1
    Accepted        = 2
    Completed       = 3
    Closed          = 4

class TaskPriority(Enum):
    Invalid         = 0
    Low             = 1
    Medium          = 2
    High            = 3
    Immediate       = 4

class Task:

    def __init__(self,id=0,requestid=0,description='', operator='', priority=TaskPriority.Invalid.value, deadline='',status=TaskStatus.Pending.value,comment=''):
        self.id = id
        self.requestID = requestid
        self.description = description
        self.operator = operator
        self.priority = priority
        self.deadline = deadline
        self.status = status
        self.comment = comment

    def setAll(self,values):
        self.id = values[0]
        self.requestID = values[1]
        self.description = values[2]
        self.operator = values[3]
        self.priority = values[4]
        self.deadline = values[5]
        self.status = values[6]
        self.comment = values[7]

    def getAll(self): return (self.id, self.requestID,self.description,self.operator,self.priority,self.deadline,self.status,self.comment)
