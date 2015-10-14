from mmse15project.database.DBInterface import DBInterface


class Model:
    def __init__(self):
        self.db = DBInterface("sepdb.db")
