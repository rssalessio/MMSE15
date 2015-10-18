

class ClientMeeting:
    def __init__(self,clientid=0, date='',comment=''):
        self.clientID=clientid
        self.date = date
        self.comment = comment

    def setAll(self,values):
        self.clientID=values[0]
        self.date = values[1]
        self.comment = values[2]

    def getAll(self): return(self.clientID,self.date,self.comment)