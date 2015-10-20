from  tests.model.ModelTests import *
import os.path

def main():
    ModelTests("test2.db")
    os.remove("test2.db")
    assert(os.path.isfile("test2.db")==False)
    print("Model test passed")
    print("All tests passed!")