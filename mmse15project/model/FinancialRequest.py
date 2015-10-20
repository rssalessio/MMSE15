from enum import Enum


class FinancialRequestStatus(Enum):
    InvalidType = 0
    Pending     = 1
    Approved    = 2
    Rejected    = 3

class FinancialRequest:
    def __init__(self, id=0, date='', department='', requestID = 0, amount = 0, reason='',
                 status=FinancialRequestStatus.Pending.value):
        self.id=id
        self.date = date
        self.department = department
        self.requestID = requestID
        self.amount = amount
        self.reason = reason
        self.status = status

    def setAll(self,values):
        self.id=values[0]
        self.date = values[1]
        self.department = values[2]
        self.requestID = values[3]
        self.amount = values[4]
        self.reason = values[5]
        self.status = values[6]

    def getAll(self):
        return (self.id,self.date,self.department,self.requestID,self.amount,self.reason,self.status)

