from  tests.model.DBTests import *
from tests.model.AccountTests import  *


def main():
    DBTest("test2.db")
    print("Database test passed")
    AccountTest()
    print("Account test passed")
    print("All tests passed!")