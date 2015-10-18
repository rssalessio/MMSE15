

class Discount:

    def __init__(self, requestid=0, amount=0, comment='', date=''):
        self.requestID = requestid
        self.amount = amount
        self.comment = comment
        self.date = date

    def setAll(self,values):
        self.requestID = values[0]
        self.amount = values[1]
        self.comment = values[2]
        self.date = values[3]
    def getAll(self): return (self.requestID,self.amount,self.comment,self.date)