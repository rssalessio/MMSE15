from  tests.model.DBTests import *
from tests.model.AccountTests import  *


def main():
    DBTest("test.db")
    print("Database test passed")
    AccountTest()
    print("Account test passed")
    print("All tests passed!")