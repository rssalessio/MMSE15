from mmse15project.model.DBConnection import  DBConnection
from mmse15project.model.Client import  Client
from mmse15project.model.DBInterface import DBInterface

class ClientDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self, client):
        values = client.getAllData().pop(0)
        self.database.executeDoQuery('INSERT INTO client (email,name,address,city,birthdate ) VALUES (?,?,?,?,?)',values)
        client.setID(self.database.getLastRow())
        return client.getID()

    def update(self,client):
        values = client.getAllData().pop(0)
        values = (values, client.getEmail())
        self.database.executeDoQuery('UPDATE client SET email=?,name = ?,address = ?,city = ? ,birthdate = ? where email=?',values)

    def get(self,client):
        ans = self.database.executeKnowQuery('SELECT * FROM client WHERE email = ?', (client.getClientID(),))[0]
        if (len(ans) == 0):
            return False
        ret = client()
        ret.setAllData(ans)
        return ret


