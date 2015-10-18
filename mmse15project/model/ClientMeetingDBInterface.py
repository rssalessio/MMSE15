
from mmse15project.model.ClientMeeting import *
from mmse15project.model.DBInterface import DBInterface
from mmse15project.model.GenericMethods import *


class ClientMeetingDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def add(self,meeting):
        values = meeting.getAll()
        self.database.executeDoQuery('INSERT INTO clientMeeting (clientID,date,comment) VALUES (?,?,?)',values)

    def update(self,meeting):
        values = meeting.getAll()
        values = tuple_without(values,0)
        values = values +(meeting.clientID,)
        self.database.executeDoQuery('UPDATE clientMeeting SET date=?,comment=? where clientID=?',values)

    def get(self,meeting):
        ans = self.database.executeKnowQuery('SELECT * FROM clientMeeting WHERE clientID = ?', (meeting.clientID,))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = ClientMeeting()
        ret.setAll(ans)
        return ret

    def getAll(self):
        ans = self.database.executeKnowQuery('SELECT * FROM clientMeeting')
        if (len(ans) == 0):
            return False
        ret = []
        for row in ans:
            temp = ClientMeeting()
            temp.setAll(row)
            ret.append(temp)
        return ret