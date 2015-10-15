
from datetime import datetime
class Schedule:
    def __init__(self,id=0, employee='', starth=0, endh=0, date=''):
        self.id = id
        self.employee = employee
        self.starthour = starth
        self.endhour = endh
        self.date = datetime.strptime(date, '%b-%d-%Y')

    def getID(self): return self.id
    def getEmployee(self): return self.employee
    def getStartHour(self): return self.starthour
    def getEndHour(self): return self.endhour
    def getDate(self): return self.date
    def getAllData(self): return (self.id, self.employee, self.starthour, self.endhour, self.date)

    def setID(self,id): self.id = id
    def setEmployee(self,e): self.employee = e
    def setStartHour(self,sh): self.starthour = sh
    def setEndHour(self,eh): self.endhour =eh
    def setDate(self,date): self.date = date
    def setAllData(self,values):
        self.id = values[0]
        self.employee = values[1]
        self.starthour = values[2]
        self.endhour = values[3]
        self.date = datetime.strptime(values[4], '%b-%d-%Y')