from mmse15project.model.Request import  Request
from mmse15project.model.DBInterface import DBInterface
from mmse15project.model.GenericMethods import  *

class RequestDBInterface (DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self, request):
        values = request.getAll()
        values =tuple_without(values,0)
        self.database.executeDoQuery('INSERT INTO request (clientID, eventType,startDate, endDate, expectedParticipants, expectedBudget, preferences, status ) VALUES (?,?,?,?,?,?,?,?)',values)
        request.setID(self.database.getLastRow())
        return request.getID()

    def update(self,request):
        values = request.getAll()
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
            req.setAll(row)
            ret.append(req)
        return ret

    def getByID(self,id):
        ans = self.database.executeKnowQuery('SELECT * FROM request WHERE id = ?', (id,))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = Request()
        ret.setAll(ans)
        return ret

    def getByClientID(self,clientid):
        temp = Request()
        temp.clientid = clientid
        return self.get(temp)

    def getAll(self):
        ans= self.database.executeKnowQuery('SELECT * from request')
        if (len(ans)==0):
            return False
        return ans

    def getByStatus(self, status):
        ans = self.database.executeKnowQuery('SELECT * FROM request WHERE status = ?', (status,))
        if (len(ans) == 0):
            return False
        ret = []
        for r in ans:
            temp = Request()
            temp.setAll(r)
            ret.append(temp)
        return ret
