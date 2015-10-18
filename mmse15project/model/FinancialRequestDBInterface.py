from mmse15project.model.FinancialRequest import *
from mmse15project.model.DBInterface import DBInterface
from mmse15project.model.GenericMethods import *

class FinancialRequestDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self, request):
        values = request.getAll()
        values = tuple_without(values,0)
        self.database.executeDoQuery('INSERT INTO financialRequest (date,department,requestID,amount,reason,status ) VALUES (?,?,?,?,?,?)',values)
        request.id= self.database.getLastRow()
        return request.id

    def update(self,request):
        values = request.getAll()
        values =tuple_without(values,0)
        values = values +  (request.id,)
        self.database.executeDoQuery('UPDATE financialRequest SET date=?,department=?,requestID=?,amount=?,reason=?,status=? where id=?',values)

    def get(self,request):
        ans = self.database.executeKnowQuery('SELECT * FROM financialRequest WHERE id = ?', (request.id,))
        if (len(ans) == 0):
            return False
        ans = ans[0]
        ret = FinancialRequest()
        ret.setAll(ans)
        return ret

    def getAll(self):
        ans= self.database.executeKnowQuery('SELECT * from financialRequest')
        if (len(ans)==0):
            return False
        ret=[]
        for row in ans:
            temp = FinancialRequest()
            temp.setAll(row)
            ret.append(temp)
        return ret

    def getByRequestID(self,requestID):
        ans = self.database.executeKnowQuery('SELECT * FROM financialRequest WHERE requestID = ?', (requestID,))
        if (ans== False):
            return False
        ret = []
        for row in ans:
            temp = FinancialRequest()
            temp.setAll(row)
            ret.append(temp)
        return ret








