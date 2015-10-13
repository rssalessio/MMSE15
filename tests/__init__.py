#!/usr/bin/env python3
from  tests.DBInterface.DBTests import *
from tests.AccountTests import  *
__author__ = ('tobias','alessior@kth.se')

def runtests():
    DBTest("test.db")
    print("Database test passed")
    AccountTest()
    print("Account test passed")
    print("All tests passed!")