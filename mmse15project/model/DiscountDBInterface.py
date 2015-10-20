
from mmse15project.model.Discount import  *
from mmse15project.model.DBInterface import DBInterface
from mmse15project.model.GenericMethods import *
class DiscountDBinterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self,discount):
        values = discount.getAll()
        self.database.executeDoQuery('INSERT INTO discount (requestID,amount,comment,date) VALUES (?,?,?,?)',values)

    def update(self,discount):
        values = discount.getAll()
        values = tuple_without(values,0)
        values = values +(discount.requestID,)
        self.database.executeDoQuery('UPDATE discount SET amount=?,comment=?, date=? where requestID=?',values)

    def get(self,discount):
        ans = self.database.executeKnowQuery('SELECT * FROM discount WHERE requestId = ?', (discount.requestID,))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = Discount()
        ret.setAll(ans)
        return ret

    def getByRequestID(self, r_id):
        temp = Discount()
        temp.requestID = r_id
        return self.get(temp)

    def existRequestID(self, r_id):
        temp = Discount()
        temp.requestID = r_id
        if self.get(temp) is False:
            return False
        else:
            return True

    def getAll(self):
        ans = self.database.executeKnowQuery('SELECT * FROM discount')
        if (len(ans) == 0):
            return False
        ret = []
        for row in ans:
            temp = Discount()
            temp.setAll(row)
            ret.append(temp)
        return ret