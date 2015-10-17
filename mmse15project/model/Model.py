from mmse15project.model.DBConnectionSQLite import DBConnectionSQLite
from mmse15project.model.AccountDBInterface import AccountDBInterface
from mmse15project.model.ClientDBInterface import ClientDBInterface

class Model:
    def __init__(self):
        self.db = DBConnectionSQLite("sepdb.db")
        self.account_db = AccountDBInterface(self.db)
        self.client_db = ClientDBInterface(self.db)

