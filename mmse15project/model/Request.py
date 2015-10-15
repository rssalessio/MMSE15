from enum import Enum
from datetime import datetime

class RequestStatus(Enum):
    invalid     = 0,
    pending     = 1,
    accepted    = 2,
    rejected    = 3

class Request:
        def __init__(self,id=0,clientid=0,eventType='', startdate='01 jan 91', enddate='01 jan 91', epar = 0, ebudg=0,pref='',status=RequestStatus.invalid):
            self.id = id
            self.clientid = clientid
            self.eventType = eventType
            self.startdate = datetime.strptime(startdate, '%b-%d-%Y')
            self.enddate  = datetime.strptime(enddate, '%b-%d-%Y')
            self.expectedParticipants = epar
            self.expectedBudget = ebudg
            self.preferences = pref
            self.status = status

        def getID(self): return self.id
        def getClientID(self): return self.clientid
        def getEventType(self): return self.eventType
        def getStartDate(self): return self.startdate
        def getEndDate(self): return self.enddate
        def getExpectedParticipants(self): return self.expectedParticipants
        def getExpectedBudget(self):return self.expectedBudget
        def getPreferences(self):return self.preferences
        def getStatus(self): return self.status
        def getAllData(self): return (self.id, self.clientid, self.eventType, self.startdate, self.enddate, self.expectedParticipants, self.expectedBudget,self.preferences,self.status)

        def setID(self,id): self.id = id
        def setClientID(self,id): self.clientid = id
        def setEventType(self,et): self.eventType=et
        def setStartDate(self,sd): self.startdate = datetime.strptime(sd, '%b-%d-%Y')
        def setEndDate(self,ed): self.enddate = datetime.strptime(ed, '%b-%d-%Y')
        def setExpectedParticipants(self,ep): self.expectedParticipants = ep
        def setExpectedBudget(self,eb): self.expectedBudget = eb
        def setPreferences(self,p): self.preferences = p
        def setStatus(self,s): self.status = s
        def setAllData(self,values):
            self.id = values[0]
            self.clientid = values[1]
            self.eventType = values[2]
            self.startdate = datetime.strptime(values[3], '%b-%d-%Y')
            self.enddate  = datetime.strptime(values[4], '%b-%d-%Y')
            self.expectedParticipants = values[5]
            self.expectedBudget = values[6]
            self.preferences = values[7]
            self.status = values[8]