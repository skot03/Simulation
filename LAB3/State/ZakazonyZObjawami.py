from .Stan import Stan
from .Odporny import Odporny
from Person import Person
import random

class ZakazonyZObjawami(Stan):
    def __init__(self):
        try:
            self.elapsed_time = 0
            self.time_to_transition = random.randint(500, 750)
        except Exception as e:
            print(f"Error initializing ZakazonyZObjawami state: {e}")
            self.elapsed_time = 0
            self.time_to_transition = random.randint(500, 750)

    def handle(self, person: Person):
        """Przetwarza czas przejścia w stan odporności."""
        try:
            self._increment_timer(person)
        except Exception as e:
            print(f"Error handling ZakazonyZObjawami state for person: {e}")

    def _increment_timer(self, person):
        """Zwiększa licznik czasu i zmienia stan agenta, jeśli to konieczne."""
        try:
            self.elapsed_time += 1
            if self.elapsed_time > self.time_to_transition:
                person.state = Odporny()
        except Exception as e:
            print(f"Error in _increment_timer method: {e}")

    def getColor(self):
        """Zwraca kolor reprezentujący stan z objawami."""
        try:
            return "#FF0000"  # Czerwony (stan z objawami)
        except Exception as e:
            print(f"Error getting color for ZakazonyZObjawami state: {e}")
            return "#FFFFFF"  # Default color in case of error
