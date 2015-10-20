from enum import Enum
from datetime import datetime


class RequestStatus(Enum):
    Rejected        = 0
    Pending         = 1  # waits CustomerService
    Accepted1       = 2  # waits Financial
    Accepted2       = 3  # waits Administration
    Accepted3       = 4  # waits details creation
    DetailsCreated  = 5


class Request:
        def __init__(self,id=0,clientid=0,eventType='', startdate='01/01/1991', enddate='01/01/1991', epar = 0, ebudg=0,pref='',status=RequestStatus.Pending.value,comment=''):
            self.id = id
            self.clientid = clientid
            self.eventType = eventType
            self.startdate = startdate
            self.enddate  = enddate
            self.expectedParticipants = epar
            self.expectedBudget = ebudg
            self.preferences = pref
            self.status = status
            self.comment = ''

        def getID(self): return self.id
        def getClientID(self): return self.clientid
        def getEventType(self): return self.eventType
        def getStartDate(self): return self.startdate
        def getEndDate(self): return self.enddate
        def getExpectedParticipants(self): return self.expectedParticipants
        def getExpectedBudget(self):return self.expectedBudget
        def getPreferences(self):return self.preferences
        def getStatus(self): return self.status
        def getAll(self): return (self.id, self.clientid, self.eventType, self.startdate, self.enddate, self.expectedParticipants, self.expectedBudget,self.preferences,self.status,self.comment)

        def setID(self,id): self.id = id
        def setClientID(self,id): self.clientid = id
        def setEventType(self,et): self.eventType=et
        def setStartDate(self,sd): self.startdate = sd
        def setEndDate(self,ed): self.enddate = ed
        def setExpectedParticipants(self,ep): self.expectedParticipants = ep
        def setExpectedBudget(self,eb): self.expectedBudget = eb
        def setPreferences(self,p): self.preferences = p
        def setStatus(self,s): self.status = s
        def setAll(self,values):
            self.id = values[0]
            self.clientid = values[1]
            self.eventType = values[2]
            self.startdate = values[3]
            self.enddate  = values[4]
            self.expectedParticipants = values[5]
            self.expectedBudget = values[6]
            self.preferences = values[7]
            self.status = values[8]
            self.comment=values[9]