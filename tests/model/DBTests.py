from mmse15project.model.DBConnectionSQLite import *
from mmse15project.model.AccountDBInterface import *
from mmse15project.model.Account import *
from mmse15project.model.ClientDBInterface import *
from mmse15project.model.Client import *
from mmse15project.model.Request import  *
from mmse15project.model.RequestDBInterface import *
def AccountDBInterfaceTest(db):
    assert (db.isConnectionOk() == 1)
    db.executeDoQuery("DROP TABLE IF EXISTS account")
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
    DBAcc.add(Account("ale@kth.se", "test", "ale", 1,1,0,'test',''))
    account = DBAcc.login('ale@kth.se', 'test')
    assert (account.getPassword() == "test")
    assert (account.getEmail() == 'ale@kth.se')
    assert (account.getName() == 'ale')
    assert (account.getAccountType() == 1)
    account.setName('bob')
    DBAcc.update(account)
    account=DBAcc.get(account)
    assert (account.getName() == 'bob')
    account = DBAcc.login("wrong","wrong")
    assert(account == False)
    print("Passed AccountDBInterface test")

def ClientDBInterfaceTest(db):
    assert (db.isConnectionOk() == 1)
    db.executeDoQuery("DROP TABLE IF EXISTS client")
    db.executeDoQuery(
        "CREATE TABLE  client (id INTEGER PRIMARY KEY AUTOINCREMENT, email text NOT NULL UNIQUE, name text  NOT NULL, address text NOT NULL ,postalCode integer,city    text NOT NULL ,birthdate text NOT NULL)")
    ClientDB = ClientDBInterface(db)
    client = Client(0,'alessior@kth.se','Alessio Russo','via la spezia 10/8', 16149, 'Genova','11/03/1991')
    client.id=ClientDB.add(client)
    assert(client.id != 0)
    client = ClientDB.get(client)
    assert(client.getName() == 'Alessio Russo')
    client.name ="Russo Alessio"
    ClientDB.update(client)
    client = ClientDB.get(client)
    assert(client.getName() == 'Russo Alessio')
    client = ClientDB.getByEmail('alessior@kth.se')
    assert(client.getName() == 'Russo Alessio')
    client = ClientDB.getByName('Alessio')
    assert(len(client)==1)
    client=client[0]
    assert(client.getName() == 'Russo Alessio')
    a = ClientDB.listOfClients()
    assert(len(a) ==1)
    print("Passed ClientDBInterface test")


def RequestDBInterfaceTest(db):
    assert (db.isConnectionOk() == 1)
    db.executeDoQuery("DROP TABLE IF EXISTS request")
    db.executeDoQuery(
        "CREATE TABLE IF NOT EXISTS request(id INTEGER PRIMARY KEY AUTOINCREMENT,clientID INTEGER,eventType text,startDate text,endDate   text,expectedParticipants integer,expectedBudget integer,preferences text,status integer,FOREIGN KEY(clientID) REFERENCES client(id))")
    reqDB = RequestDBInterface(db)
    print("Passed RequestDBInterface test")

def DBTest(connection_name):
    db = DBConnectionSQLite(connection_name)
    AccountDBInterfaceTest(db)
    ClientDBInterfaceTest(db)
    RequestDBInterfaceTest(db)
