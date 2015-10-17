from mmse15project.model.DBConnectionSQLite import DBConnectionSQLite

class Model:
    def __init__(self):
        self.db = DBConnectionSQLite("sepdb.db")
