from mmse15project.model.DBConnectionSQLite import *
from mmse15project.model.DBInterfaceAccount import *
from mmse15project.model.Account import *


def DBTest(connectionName):
    db = DBInterface(connectionName)
    assert (db.isConnectionOk() == 1)
    db.executeDoQuery("DROP TABLE account")
    db.executeDoQuery(
        "CREATE TABLE IF NOT EXISTS account (email text PRIMARY KEY, password text, name text, accountType INTEGER)")
    db.executeDoQuery(
        "INSERT INTO account (email,password,name,accountType) VALUES ('test@kth.se','password','Alessio','1')")
    DBAcc = DBInterfaceAccount(db)
    account = DBAcc.login('test@kth.se', 'password')
    assert (account.getPassword() == "password")
    assert (account.getEmail() == 'test@kth.se')
    assert (account.getName() == 'Alessio')
    assert (account.getAccountType() == 1)
    DBAcc.addAccount(Account("ale@kth.se", "test", "ale", 1))
    account = DBAcc.login('ale@kth.se', 'test')
    assert (account.getPassword() == "test")
    assert (account.getEmail() == 'ale@kth.se')
    assert (account.getName() == 'ale')
    assert (account.getAccountType() == 1)
