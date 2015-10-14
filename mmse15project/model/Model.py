from mmse15project.database.DBInterface import DBInterface

__author__ = 'tobias'


class Model:
    def __init__(self):
        self.db = DBInterface("sepdb.db")
