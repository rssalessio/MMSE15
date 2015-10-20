from mmse15project.model.DBConnection import  DBConnection
from mmse15project.model.Account import  Account
from mmse15project.model.DBInterface import DBInterface
# DBInterfaceAccount  is  a layer above DBConnection, it defines basic functions that interact with the database about matters regarding
#the user account
#
#Variables: database: connection to the database
#
#Functions:
#login(email,password): check if the user account is present in the database. If not False is returned, otherwise an Account object is returned
#addAccount(account): given the Account object, it is added to the database.
#updateAccount(account): updates the data of an account given the account object. Can't change the email


class AccountDBInterface(DBInterface):
    def __init__(self,database):
        self.database = database

    def login(self, email, pwd):
        values= (email,pwd)
        ans = self.database.executeKnowQuery('SELECT * FROM account WHERE email = ? and password = ?', values)
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = Account()
        ret.setAll(ans)
        return ret

    def add(self,account):
        values = (account.getEmail(), account.getPassword(), account.getName(), account.getAccountType(),
                  account.getAccountTeam(), account.getAccountQualification(), account.getDepartment(), account.getComment())
        self.database.executeDoQuery('INSERT INTO account (email,password,name,accountType,accountTeam,accountQualification,department,comment) VALUES (?,?,?,?,?,?,?,?)',values)

    def update(self,account):
        values = (account.getEmail(), account.getPassword(), account.getName(), account.getAccountType(),
                  account.getAccountTeam(), account.getAccountQualification(), account.getDepartment(), account.getComment(),account.getEmail())
        self.database.executeDoQuery('UPDATE account SET email= ?, password= ? , name = ? , accountType = ?, accountTeam = ?, accountQualification=?, department = ?, comment = ? where email = ?',values)

    def get(self,account):
        ans = self.database.executeKnowQuery('SELECT * FROM account WHERE email = ?', (account.getEmail(),))
        if (len(ans) == 0):
            return False
        ans=ans[0]
        ret = Account()
        ret.setAll(ans)
        return ret

    def getByEmail(self, email):
        temp = Account()
        temp.email = email
        return self.get(temp)