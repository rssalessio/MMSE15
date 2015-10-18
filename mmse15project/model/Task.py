from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    invalid         = 0
    pending         = 1
    accepted        = 2
    completed       = 3
    other           = 4

class TaskPriority(Enum):
    invalid         = 0
    low             = 1
    medium          = 2
    high            = 3
    immediate       = 4

class Task:

    def __init__(self,requestid=0,description='', operator='', priority=TaskPriority.invalid.value, deadline='',status=TaskStatus.invalid.value,comment=''):
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
