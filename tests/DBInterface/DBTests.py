from mmse15project.database.DBInterface import *


def DBTest(connectionName):
    db = DBInterface(connectionName)
    assert(db.isConnectionOk() == 1)
    db.executeCommand("DROP TABLE account")
    db.executeCommand("CREATE TABLE IF NOT EXISTS account (username text PRIMARY KEY, password text, email text, name text)")
    db.executeCommand("INSERT INTO account VALUES ('admin','password','test@kth.se','Alessio')")
    rows = db.login('admin','password')
    assert(len(rows) ==1)
    assert(rows[0][0] == 'admin' and rows[0][1] == 'password' and
           rows[0][2] == 'test@kth.se' and rows[0][3]=='Alessio')
