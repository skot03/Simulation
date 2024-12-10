from .Stan import Stan
from .Odporny import Odporny
from Person import Person
import random

class ZakazonyBezObjawow(Stan):
    def __init__(self):
        try:
            self.czas_obsluga = 0
            self.czas_do_zmiany = random.randint(500, 750)
        except Exception as e:
            print(f"Error initializing ZakazonyBezObjawow state: {e}")
            self.czas_obsluga = 0
            self.czas_do_zmiany = random.randint(500, 750)

    def _licznik(self, person):
        """Zwiększa licznik czasu i zmienia stan agenta, jeśli to konieczne."""
        try:
            self.czas_obsluga += 1
            if self.czas_obsluga > self.czas_do_zmiany:
                person.state = Odporny()
        except Exception as e:
            print(f"Error in _licznik method: {e}")

    def getColor(self):
        """Zwraca kolor reprezentujący stan bezobjawowy."""
        try:
            return "#FFA500"  # Żółty (stan bezobjawowy)
        except Exception as e:
            print(f"Error getting color for ZakazonyBezObjawow state: {e}")
            return "#FFFFFF"  # Default color in case of error

    def handle(self, person: Person):
        """Przetwarza czas przejścia w stan odporności."""
        try:
            self._licznik(person)
        except Exception as e:
            print(f"Error handling ZakazonyBezObjawow state for person: {e}")
