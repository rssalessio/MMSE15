from mmse15project.model.Model import Model
from mmse15project.views.MainView import MainView
from mmse15project.ctrls.MainController import MainController
from mmse15project.views.Login import Login
from mmse15project.model.DBConnectionSQLite import *

def main():
    database = DBConnectionSQLite("sepdb.db")
    m = Model()
    v = MainView()
    c = MainController(m, v, database)

    c.set_frame(Login)
    v.mainloop()

