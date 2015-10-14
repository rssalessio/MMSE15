from mmse15project.model.DBConnection import  DBConnection
from mmse15project.model.Account import  Account
# DBInterfaceAccount  is  a layer above DBConnection, it defines basic functions that interact with the database about matters regarding
#the user account
#
#Variables: database: connection to the database
#
#Functions:
#login(email,password): check if the user account is present in the database. If not False is returned, otherwise an Account object is returned
#addAccount(account): given the Account object, it is added to the database.


class DBInterfaceAccount:
    def __init__(self,database):
        self.database = database

    def login(self, email, pwd):
        values= (email,pwd)
        ans = self.database.executeKnowQuery('SELECT email,password, name, accountType FROM account WHERE email = ? and password = ?', values)[0]
        if (len(ans) == 0):
            return False
        return Account(ans[0],ans[1],ans[2],ans[3])

    def addAccount(self,account):
        values = (account.getEmail(), account.getPassword(), account.getName(), account.getAccountType())
        self.database.executeDoQuery('INSERT INTO account (email,password,name,accountType) VALUES (?,?,?,?)',values)