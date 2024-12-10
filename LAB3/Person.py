from Vector import Vector2D
import random
from State import *

class Person:
    def __init__(self, x, y, state: Stan, simulation):
        try:
            self.state = state
            self.simulation = simulation
            self._initialize_velocity()
            self.x = x
            self.y = y
        except Exception as e:
            print(f"Initialization Error: {e}")

    def _initialize_velocity(self):
        """Inicjalizuje prędkość agenta."""
        try:
            while True:
                move_y = random.uniform(-2.5, 2.5) / 25
                move_x = random.uniform(-2.5, 2.5) / 25
                if move_x ** 2 + move_y ** 2 <= 6.25:
                    self.speed = Vector2D(move_x, move_y)
                    break
        except Exception as e:
            print(f"Error initializing velocity: {e}")
            self.speed = Vector2D(0, 0)  # Domyślna prędkość w przypadku błędu

    def przemieszcz(self, height, width):
        """Przemieszcza agenta na podstawie prędkości."""
        try:
            new_x = self.x + self.speed.getX()
            new_y = self.y + self.speed.getY()

            if not self._is_within_bounds(new_x, new_y, width, height):
                return True

            self.x, self.y = new_x, new_y
            self.state.handle(self)
            return False
        except Exception as e:
            print(f"Error moving agent: {e}")
            return False

    def getColor(self):
        """Zwraca kolor reprezentujący aktualny stan agenta."""
        try:
            return self.state.getColor()
        except Exception as e:
            print(f"Error getting color: {e}")
            return "#FFFFFF"  # Domyślny kolor w przypadku błędu

    def _is_within_bounds(self, x, y, width, height):
        """Sprawdza, czy agent pozostaje w granicach."""
        try:
            if x < 0 or x >= width:
                if random.random() < 0.5:
                    self.speed.setComponents(-self.speed.getX(), self.speed.getY())
                else:
                    return False

            if y < 0 or y >= height:
                if random.random() < 0.5:
                    self.speed.setComponents(self.speed.getX(), -self.speed.getY())
                else:
                    return False

            return True
        except Exception as e:
            print(f"Error checking bounds: {e}")
            return False
