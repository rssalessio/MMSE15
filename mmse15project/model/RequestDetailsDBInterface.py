from mmse15project.model.RequestDetails import *
from mmse15project.model.DBInterface import *
from mmse15project.model.GenericMethods import  *

class RequestDetailsDBInterface (DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self, request):
        values = request.getAll()
        self.database.executeDoQuery('INSERT INTO requestDetails (id,detail1,detail2,detail3,detail4,detail5,detail6,needs) VALUES (?,?,?,?,?,?,?,?)',values)
        request.id=self.database.getLastRow()
        return request.id

    def update(self,request):
        values = request.getAll()
        values =tuple_without(values,0)
        values = values+  (request.id,)
        self.database.executeDoQuery('UPDATE requestDetails SET detail1=?,detail2=?,detail3=?,detail4=?,detail5=?,detail6=?,needs=? where id=?',values)

    def get(self,request):
        ans = self.database.executeKnowQuery('SELECT * FROM requestDetails WHERE id = ?', (request.id,))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = RequestDetails()
        ret.setAll(ans)
        return ret

    def getByID(self,id):
        request = RequestDetails()
        request.id = id
        return self.get(request)

    def getAll(self):
        ans= self.database.executeKnowQuery('SELECT * from requestDetails')
        if (len(ans)==0):
            return False
        ret=[]
        for row in ans:
            temp = RequestDetails()
            temp.setAll(row)
            ret.append(temp)
        return ret
