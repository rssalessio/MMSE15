__author__ = ('tobias','alessior@kth.se')
from abc import ABCMeta, abstractmethod
# DBConnection  is  an abstract class defining the basic methods to communicate with a SQL database
#
#Variables: None
#
#Functions:
#getConnectionName(): returns connectionName(check init)
#isConnectionOk(): return true if the connection with the database is ok, 0 otherwise
#executeDoCommand(query): execute generic sql do query
#executeKnowCommand(query): execute generic sql select query
#

class DBConnection:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getConnectionName(self): raise NotImplementedError()
    @abstractmethod
    def isConnectionOk(self): raise NotImplementedError()
    @abstractmethod
    def executeDoQuery(self,query,var=()): raise NotImplementedError()
    @abstractmethod
    def executeKnowQuery(self,query,var): raise NotImplementedError()