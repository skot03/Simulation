import matplotlib.pyplot as plt
import numpy as np
import random
from State import *
import copy
from Memento import *
from Person import Person


class Simulation:
    def __init__(self, sim_height, sim_width, sim_num_population, sim_scenario):
        try:
            self.width = sim_width
            self.height = sim_height
            self.scenario = sim_scenario
            self.num_population = sim_num_population
            self.fig, self.ax = self._setup_figure()
            self.scatter = self.ax.scatter([], [], c="black", s=60)
            self.population = self._initialize_population()


        except Exception as e:
            print(f"Initialization Error: {e}")

    def _initialize_population(self):
        """Inicjalizuje populację osób w zależności od scenariusza."""
        try:
            return [
                Person(random.randint(0, self.width - 1),
                       random.randint(0, self.height - 1),
                       self._determine_initial_state(),
                       self)
                for _ in range(self.num_population)
            ]
        except Exception as e:
            print(f"Population Initialization Error: {e}")
            return []

    def _determine_initial_state(self):
        """Wybiera początkowy stan osoby na podstawie scenariusza."""
        try:
            if self.scenario == 1:
                return ZdrowaOsoba()
            return Odporny() if random.random() < 0.2 else ZdrowaOsoba()
        except Exception as e:
            print(f"Determine State Error: {e}")
            return ZdrowaOsoba()

    def _setup_figure(self):
        """Tworzy i konfiguruje wygląd wykresu symulacji."""
        try:
            fig, ax = plt.subplots()
            ax.set_xlim(0, self.width)
            ax.set_ylim(0, self.height)
            fig.patch.set_facecolor('gray')
            ax.set_facecolor('gray')

            self._style_axes(ax)
            return fig, ax
        except Exception as e:
            print(f"Figure Setup Error: {e}")
            return None, None

    def _style_axes(self, ax):
        """Usuwa osie i ich elementy."""
        try:
            ax.axis('off')
        except Exception as e:
            print(f"Style Axes Error: {e}")

    def init(self):
        """Inicjalizuje dane dla matplotlib."""
        try:
            self.scatter.set_offsets(np.empty((0, 2)))
            return self.scatter,
        except Exception as e:
            print(f"Init Error: {e}")
            return self.scatter,

    def update(self, frame):
        """Aktualizuje stany populacji oraz ich pozycje na wykresie."""
        try:
            self._update_population_positions()
            if random.random() < 0.2:
                self.add_person()
            self._update_scatter_data()
            return self.scatter,
        except Exception as e:
            print(f"Update Error: {e}")
            return self.scatter,

    def get_state(self):
        """Zwraca obecny stan symulacji w formie słownika."""
        try:
            return {
                "width": self.width,
                "height": self.height,
                "population": copy.deepcopy(self.population),
            }
        except Exception as e:
            print(f"Get State Error: {e}")
            return {}

    def set_state(self, state):
        """Ustawia stan symulacji na podstawie podanego słownika."""
        try:
            self.width = state["width"]
            self.height = state["height"]
            self.population = state["population"]
        except Exception as e:
            print(f"Set State Error: {e}")

    def create_memento(self):
        """Tworzy memento obecnego stanu symulacji."""
        try:
            return Migawka(copy.deepcopy(self.get_state()))
        except Exception as e:
            print(f"Create Memento Error: {e}")
            return None

    def restore_memento(self, memento):
        """Przywraca stan symulacji z memento."""
        try:
            restored_state = copy.deepcopy(memento.get_state())
            self.set_state(restored_state)
        except Exception as e:
            print(f"Restore Memento Error: {e}")


    def _update_population_positions(self):
        """Aktualizuje pozycje osób i usuwa te, które wychodzą poza obszar."""
        try:
            for person in self.population[:]:
                if person.przemieszcz(self.height, self.width):
                    self.population.remove(person)
        except Exception as e:
            print(f"Update Population Positions Error: {e}")

    def _update_scatter_data(self):
        """Aktualizuje dane do wyświetlenia na wykresie."""
        try:
            positions = np.array([[person.x, person.y] for person in self.population])
            colors = [person.getColor() for person in self.population]
            self.scatter.set_offsets(positions)
            self.scatter.set_color(colors)
        except Exception as e:
            print(f"Update Scatter Data Error: {e}")

    def add_person(self):
        """Dodaje nową osobę w losowym położeniu wzdłuż krawędzi lub środka."""
        try:
            state = self._generate_new_person_state()
            position = self._generate_random_position()
            self.population.append(Person(position[0], position[1], state, self))
        except Exception as e:
            print(f"Add Person Error: {e}")

    def _generate_new_person_state(self):
        """Generuje stan dla nowo dodawanej osoby."""
        try:
            if random.random() < 0.1:
                return ZakazonyBezObjawow() if random.random() < 0.5 else ZakazonyZObjawami()
            if self.scenario == 2 and random.random() < 0.1:
                return Odporny()
            return ZdrowaOsoba()
        except Exception as e:
            print(f"Generate New Person State Error: {e}")
            return ZdrowaOsoba()

    def _generate_random_position(self):
        """Generuje losową pozycję osoby (również wewnątrz obszaru)."""
        try:
            if random.random() < 0.25:
                return random.randint(0, self.width), 0  # Dolna krawędź
            elif random.random() < 0.5:
                return self.width, random.randint(0, self.height)  # Prawa krawędź
            elif random.random() < 0.75:
                return random.randint(0, self.width), self.height  # Górna krawędź
            else:
                return random.randint(0, self.width), random.randint(0, self.height)  # Wewnątrz
        except Exception as e:
            print(f"Generate Random Position Error: {e}")
            return 0, 0

