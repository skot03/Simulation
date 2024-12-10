class ZapisStanow:
    def __init__(self, simulation):
        self.simulation = simulation
        self.mementos = []

    def save(self):
        """Zapisuje bieżący stan symulacji do mementa."""
        try:
            memento = self.simulation.create_memento()
            self.mementos.append(memento)
            print(f"Udalo sie zapisac nr: {len(self.mementos)}")
        except Exception as e:
            print(f"Error saving state: {e}")

    def restore(self, index):
        """Przywraca stan symulacji z zapisanego memento."""
        try:
            if index < 0 or index >= len(self.mementos):
                raise IndexError("Index out of range for mementos.")
            self.simulation.restore_memento(self.mementos[index])
            print(f"Stan przywrócony z zapisu nr: {index + 1}")
        except IndexError as e:
            print(f"Error restoring state: {e}")
        except Exception as e:
            print(f"Unexpected error during restore: {e}")
