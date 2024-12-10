from .Stan import Stan
from Person import Person

class Odporny(Stan):
    def getColor(self):
        """Zwraca kolor reprezentujący stan odporności."""
        return "#0000FF"  # Niebieski (odporność)

    def handle(self, person: Person):
        """Brak działań, gdy agent jest odporny."""
        pass
