from abc import ABC, abstractmethod

class Stan(ABC):
    @abstractmethod
    def getColor(self):
        pass
    @abstractmethod
    def handle(self, person):
        pass



