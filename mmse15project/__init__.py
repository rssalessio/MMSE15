from mmse15project.model.Model          import Model
from mmse15project.views.MainView       import MainView
from mmse15project.ctrls.MainController import MainController

__author__ = 'tobias'


def main():
    m = Model()
    v = MainView()
    c = MainController(m, v)
    v.mainloop()