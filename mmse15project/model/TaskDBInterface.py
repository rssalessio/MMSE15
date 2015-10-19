
from mmse15project.model.Task import *
from mmse15project.model.DBInterface import DBInterface
from mmse15project.model.GenericMethods import *

class TaskDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self,task):
        values = task.getAll()
        self.database.executeDoQuery('INSERT INTO task (requestID,description,operator,priority,deadline,status,comment) VALUES (?,?,?,?,?,?,?)',values)

    def update(self,task):
        values = task.getAll()
        values = tuple_without(values,0)
        values = values +(task.requestID,)
        self.database.executeDoQuery('UPDATE task SET description=?,operator=?,priority=?,deadline=?,status=?,comment=? where requestID=?',values)

    def get(self,task):
        ans = self.database.executeKnowQuery('SELECT * FROM task WHERE requestID = ?', (task.requestID,))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = Task()
        ret.setAll(ans)
        return ret

    def getAll(self):
        ans = self.database.executeKnowQuery('SELECT * FROM task')
        if (len(ans) == 0):
            return False
        ret = []
        for row in ans:
            temp = Task()
            temp.setAll(row)
            ret.append(temp)
        return ret

    def getByRequestID(self,id):
        temp = Task(id,'','',TaskPriority.invalid.value,'',TaskStatus.invalid.value,'')
        return self.get(temp)

    def getByStatus(self,status):
        ans = self.database.executeKnowQuery('SELECT * FROM task WHERE status = ?', (status,))
        if (len(ans) == 0):
            return False
        ret = []
        for r in ans:
            temp = Task()
            temp.setAll(r)
            ret.append(temp)
        return ret

    def getByStatusAndEmail(self, status, email):
        correct_status = self.getByStatus(status)
        ret = []
        for task in correct_status:
            print(task.operator)
            print(email)
            if task.operator == email:
                ret.append(task)
        return ret
