from mmse15project.model.DBConnection import  DBConnection
from mmse15project.model.Client import  Client
from mmse15project.model.DBInterface import DBInterface

class ClientDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self, client):
        values = client.getAllData()
        values = tuple(filter(lambda el: el != client.getID(), values))
        self.database.executeDoQuery('INSERT INTO client (email,name,address,postalCode,city,birthdate ) VALUES (?,?,?,?,?,?)',values)
        client.setID(self.database.getLastRow())
        return client.getID()

    def update(self,client):
        values = client.getAllData()
        values = tuple(filter(lambda el: el != client.getID(), values))
        values = values +  (client.getEmail(),)
        self.database.executeDoQuery('UPDATE client SET email=?,name = ?,address = ?,postalCode=?,city = ? ,birthdate = ? where email=?',values)

    def get(self,client):
        ans = self.database.executeKnowQuery('SELECT * FROM client WHERE email = ?', (client.getEmail(),))
        if (len(ans) == 0):
            return False
        ans = ans[0]
        ret = Client()
        ret.setAllData(ans)
        return ret

    def getByEmail(self,email):
        temp = Client()
        temp.email = email
        return self.get(temp)

    def getByName(self,name):
        ans = self.listOfClients()
        ret = []
        for row in ans:
            if (name not in row[2]) : continue
            temp = Client()
            temp.setAllData(row)
            ret.append(temp)
        return ret

    def listOfClients(self):
        return self.database.executeKnowQuery('SELECT * from client')





