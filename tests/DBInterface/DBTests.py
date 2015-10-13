__author__ = 'alessior@kth.se'
from mmse15project.database.DBInterface import *


def DBTest(connectionName):
    db = DBInterface(connectionName)
    assert(db.isConnectionOk() == 1)
