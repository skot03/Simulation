from abc import ABC, abstractmethod


class IVector(ABC):

    @abstractmethod
    def abs(self) -> float:
        """Zwraca długość wektora."""
        pass

    @abstractmethod
    def cdot(self, param: 'IVector') -> float:
        """Zwraca iloczyn skalarny z innym wektorem."""
        pass

    @abstractmethod
    def getComponents(self) -> list:
        """Zwraca komponenty wektora w postaci listy."""
        pass

    @abstractmethod
    def setComponents(self, x: float, y: float):
        """Ustala komponenty wektora."""
        pass

    @abstractmethod
    def getX(self) -> float:
        """Zwraca komponent X wektora."""
        pass

    @abstractmethod
    def getY(self) -> float:
        """Zwraca komponent Y wektora."""
        pass
