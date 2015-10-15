from datetime import datetime





class Client:
    def __init__(self, id=0,email = '', name ='', address='', city='', birthdate='1 jan 91'):
        self.id=id
        self.email = email
        self.name = name
        self.address = address
        self.city = city
        self.birthdate =  datetime.strptime(birthdate, '%b-%d-%Y')


    def setAllData(self,values):
        self.id = values[0]
        self.email = values[1]
        self.name = values[2]
        self.address = values[4]
        self.city = values[4]
        self.birthdate = datetime.strptime(values[5], '%b-%d-%Y')

    def getAllData(self,values): return (self.id,self.email,self.name,self.address,self.city,self.birthdate)

    def getID(self): return self.id
    def getEmail(self): return self.email
    def getName(self): return self.name
    def getAddress(self): return self.address
    def getCity(self): return self.city
    def getBirthDate(self): return self.birthdate

    def setID(self,id): self.id = id
    def setEmail(self,email): self.email = email
    def setName(self,name): self.name = name
    def setAddress(self,address): self.address = address
    def setCity(self): self.city
    def setBirthDate(self, bd): self.birthdate = datetime.strptime(birthdate, '%b-%d-%Y')