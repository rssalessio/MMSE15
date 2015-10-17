from mmse15project.model.DBConnectionSQLite import DBConnectionSQLite
from mmse15project.model.AccountDBInterface import AccountDBInterface
from mmse15project.model.Account import Account
from mmse15project.model.Account import AccountQualification
from mmse15project.model.Account import AccountTeam
from mmse15project.model.Account import AccountType


class Model:
    def __init__(self):
        self.db = DBConnectionSQLite("sepdb.db")
        self.accountDB = AccountDBInterface(self.database)

