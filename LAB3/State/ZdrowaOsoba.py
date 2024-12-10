import math
import random
from .Stan import Stan
from .ZakazonyZObjawami import ZakazonyZObjawami
from .ZakazonyBezObjawow import ZakazonyBezObjawow


class ZdrowaOsoba(Stan):
    def __init__(self):
        try:
            self.lista = {}
        except Exception as e:
            print(f"Error initializing the state list: {e}")

    def getColor(self):
        """Zwraca kolor dla stanu Healthy."""
        try:
            return "#00FF00"
        except Exception as e:
            print(f"Error getting color: {e}")
            return "#FFFFFF"  # Zwracamy domyślny kolor, jeśli wystąpi błąd

    def handle(self, person):
        """Obsługuje logikę kontaktów i zmienia stan osoby."""
        try:
            lista_person = []
            id_osoby = 0

            while id_osoby < len(person.simulation.population):
                inny = person.simulation.population[id_osoby]

                # Pomijamy siebie samego
                if inny is person:
                    id_osoby += 1
                    continue

                # Obliczamy dystans
                try:
                    odleglosc = math.dist((person.x, person.y), (inny.x, inny.y))
                except Exception as e:
                    print(f"Error calculating distance between person {person} and {inny}: {e}")
                    odleglosc = float('inf')  # Jeśli wystąpi błąd, traktujemy dystans jako nieskończoność

                # Jeżeli dystans jest mniejszy lub równy 2, sprawdzamy stan
                if odleglosc <= 2 and isinstance(inny.state, (ZakazonyZObjawami, ZakazonyBezObjawow)):
                    # Aktualizujemy timer kontaktu dla innych osób
                    self.lista.setdefault(inny, 0)
                    self.lista[inny] += 1

                    if self.lista[inny] >= 75:
                        try:
                            if isinstance(inny.state, ZakazonyZObjawami):
                                person.state = ZakazonyZObjawami() if random.random() < 0.5 else ZakazonyBezObjawow()
                            else:
                                person.state = ZakazonyZObjawami() if random.random() < 0.5 else ZakazonyBezObjawow()
                        except Exception as e:
                            print(f"Error changing state of person {person}: {e}")
                        break  # Wyjście z pętli po zmianie stanu
                else:
                    if inny in self.lista:
                        lista_person.append(inny)

                id_osoby += 1

            zmien = 0
            while zmien < len(lista_person):
                ktoregoUsunac = lista_person[zmien]
                try:
                    if ktoregoUsunac in self.lista:
                        self.lista.pop(ktoregoUsunac, None)
                except Exception as e:
                    print(f"Error removing person {ktoregoUsunac} from contact list: {e}")
                zmien += 1

        except Exception as e:
            print(f"Error handling the person state: {e}")
