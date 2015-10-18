
from mmse15project.model.Schedule import *
from mmse15project.model.DBInterface import DBInterface
from mmse15project.model.GenericMethods import *


class ScheduleDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self,schedule):
        values = schedule.getAll()
        values = tuple_without(values,0)
        self.database.executeDoQuery('INSERT INTO schedule (employee,startHour,endHour,date) VALUES (?,?,?,?)',values)
        schedule.id= self.database.getLastRow()
        return schedule.id

    def update(self,schedule):
        values = schedule.getAll()
        values = tuple_without(values,0)
        values = values +(schedule.id,)
        self.database.executeDoQuery('UPDATE schedule SET employee=?,startHour=?,endHour=?,date=? where id=?',values)

    def get(self,schedule):
        ans = self.database.executeKnowQuery('SELECT * FROM schedule WHERE employee = ?', (schedule.employee,))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = Schedule()
        ret.setAll(ans)
        return ret

    def getAll(self):
        ans = self.database.executeKnowQuery('SELECT * FROM schedule')
        if (len(ans) == 0):
            return False
        ret = []
        for row in ans:
            temp = Schedule()
            temp.setAll(row)
            ret.append(temp)
        return ret