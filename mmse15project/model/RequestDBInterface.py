from mmse15project.model.DBConnection import  DBConnection
from mmse15project.model.Request import  Request
from mmse15project.model.DBInterface import DBInterface
from mmse15project.GenericMethods import  *

class RequestDBInterface (DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self, request):
        values = request.getAllData()
        values =tuple_without(values,0)
        self.database.executeDoQuery('INSERT INTO request (clientID, eventType,startDate, endDate, expectedParticipants, expectedBudget, preferences, status ) VALUES (?,?,?,?,?,?,?,?)',values)
        request.setID(self.database.getLastRow())
        return request.getID()

    def update(self,request):
        values = request.getAllData()
        values =tuple_without(values,0)
        values = values+  (request.getID(),)
        self.database.executeDoQuery('UPDATE request SET clientID=?, eventType=?,startDate=?, endDate=?, expectedParticipants=?, expectedBudget=?, preferences=?, status=? where id=?',values)

    def get(self,request):
        ans = self.database.executeKnowQuery('SELECT * FROM request WHERE clientID = ?', (request.getClientID(),))
        if (len(ans) == 0):
            return False
        ret = []
        for row in ans:
            req = Request()
            req.setAllData(row)
            ret.append(req)
        return ret

    def getByID(self,id):
        ans = self.database.executeKnowQuery('SELECT * FROM request WHERE id = ?', (id,))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = Request()
        ret.setAllData(ans)
        return ret

    def getByClientID(self,clientid):
        temp = Request()
        temp.clientid = clientid
        return self.get(temp)
