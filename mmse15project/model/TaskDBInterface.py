
from mmse15project.model.Task import *
from mmse15project.model.DBInterface import DBInterface
from mmse15project.model.GenericMethods import *

class TaskDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self,task):
        values = task.getAll()
        values = tuple_without(values,0)
        self.database.executeDoQuery('INSERT INTO task (requestID,description,operator,priority,deadline,status,comment) VALUES (?,?,?,?,?,?,?)',values)
        task.id=self.database.getLastRow()
        return task.id

    def update(self,task):
        values = task.getAll()
        values = tuple_without(values,0)
        values = values +(task.id,)
        self.database.executeDoQuery('UPDATE task SET requestID=?,description=?,operator=?,priority=?,deadline=?,status=?,comment=? where id=?',values)

    def get(self,task):
        ans = self.database.executeKnowQuery('SELECT * FROM task WHERE requestID = ?', (task.requestID,))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = Task()
        ret.setAll(ans)
        return ret

    def getByID(self, t_id):
        ans = self.database.executeKnowQuery('SELECT * FROM task WHERE id = ?', (t_id,))
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

    def getByRequestID(self, r_id):
        ans = self.database.executeKnowQuery('SELECT * FROM task WHERE requestID = ?', (r_id,))
        if (len(ans) == 0):
            return False
        ret = []
        for r in ans:
            temp = Task()
            temp.setAll(r)
            ret.append(temp)
        return ret

    def getByStatus(self,status):
        ans = self.database.executeKnowQuery('SELECT * FROM task WHERE status = ?', (status,))
        if (len(ans) == 0):
            return []
        ret = []
        for r in ans:
            temp = Task()
            temp.setAll(r)
            ret.append(temp)
        return ret

    def getByStatusAndEmail(self, status, email):
        correct_status = self.getByStatus(status)
        if correct_status is False:
            return []
        ret = []
        for task in correct_status:
            if task.operator == email:
                ret.append(task)
        if (len(ret)==0): return False
        return ret

    def getByTaskID(self,id):
        ans = self.database.executeKnowQuery('SELECT * FROM task WHERE id = ?', (id,))[0]
        if (len(ans) == 0):
            return False
        ret = Task()
        ret.setAll(ans)
        return ret

    def getTasksByAccTypeUser(self, acc_type, user):
        if acc_type == "Manager":
            tasks =[]
            for num in range(1,3):
                t = self.getByStatus(num)
                if (t == False): continue
                tasks = tasks + t
        else:
            tasks =[]
            for num in range(1,3):
                t = self.getByStatusAndEmail(num,user)
                if (t == False): continue
                tasks = tasks + t
        return tasks

