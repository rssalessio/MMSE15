from mmse15project.model.DBConnectionSQLite import *
from mmse15project.model.AccountDBInterface import *
from mmse15project.model.Account import *


def DBTest(connection_name):
    db = DBConnectionSQLite(connection_name)
    assert (db.isConnectionOk() == 1)
    db.executeDoQuery("DROP TABLE account")
    db.executeDoQuery(
        "CREATE TABLE  account (email text PRIMARY KEY, password text,name text,accountType INTEGER,accountTeam INTEGER,accountQualification INTEGER, department text,comment text)")
    db.executeDoQuery(
        "INSERT INTO account (email,password,name,accountType,accountTeam,accountQualification,department,comment) VALUES ('test@kth.se','password','Alessio',1,1,1,'management','')")
    DBAcc = AccountDBInterface(db)
    account = DBAcc.login('test@kth.se', 'password')
    assert (account.getPassword() == "password")
    assert (account.getEmail() == 'test@kth.se')
    assert (account.getName() == 'Alessio')
    assert (account.getAccountType() == 1)
    DBAcc.addAccount(Account("ale@kth.se", "test", "ale", 1,1,0,'test',''))
    account = DBAcc.login('ale@kth.se', 'test')
    assert (account.getPassword() == "test")
    assert (account.getEmail() == 'ale@kth.se')
    assert (account.getName() == 'ale')
    assert (account.getAccountType() == 1)
    account.setName('bob')
    DBAcc.updateAccount(account)
    account=DBAcc.getAccount(account)
    assert (account.getName() == 'bob')