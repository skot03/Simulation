from .IVector import IVector

class Vector2D(IVector):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def abs(self) -> float:
        """Zwraca długość wektora."""
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def cdot(self, vec: 'Vector2D') -> float:
        """Zwraca iloczyn skalarny wektora z innym wektorem."""
        return self._x * vec.getX() + self._y * vec.getY()

    def getComponents(self) -> list:
        """Zwraca komponenty wektora jako listę."""
        return [self._x, self._y]

    def setComponents(self, x: float, y: float):
        """Ustawia nowe wartości komponentów wektora."""
        self._x = x
        self._y = y

    def getX(self) -> float:
        """Zwraca komponent X wektora."""
        return self._x

    def getY(self) -> float:
        """Zwraca komponent Y wektora."""
        return self._y
