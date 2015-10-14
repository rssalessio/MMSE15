from mmse15project.model.DBConnectionSQLite import *

class Model:
    def __init__(self):
        self.db = DBConnectionSQLite("sep.db")
