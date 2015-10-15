from  mmse15project.model.DBConnection import DBConnection
import sqlite3
# DBConnectionSQLite is  an interface class done to ease the communication with the underlying database system. It's the main interface
#to a sqlite database, it's a specialization of DBConnection
#
#Variables:
#-connectionName: string specifying the uri of the database
#-connection: connection object, check sqlite3
#-cursor: cursor object, check sqllite3
#
#functions: check DBConnection


class DBConnectionSQLite(DBConnection):
    def __init__(self, connectionName):
        self.connectionName = connectionName
        self.connection = sqlite3.connect(self.connectionName)
        if (self.connection != None):
            self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def getConnectionName(self):
        return self.connectionName

    def isConnectionOk(self):
        #actually it doesn't check if the connection is ok when it is invoked
        return  0  if  self.connection == None else 1

    def executeDoQuery(self,query,var=()):
        self.cursor.execute(query,var)
        self.connection.commit()

    def executeKnowQuery(self,query,var=()):
        return self.cursor.execute(query,var).fetchall()




