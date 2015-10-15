from abc import ABCMeta, abstractmethod

class DBInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self): raise NotImplementedError()
    @abstractmethod
    def update(self): raise NotImplementedError()
    @abstractmethod
    def get(self,query,var=()): raise NotImplementedError()