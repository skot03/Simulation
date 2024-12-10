
from Simulation import Simulation
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from Memento import *
import tkinter as tk
from tkinter import filedialog  # Do wybrania lokalizacji zapisu pliku
import numpy as np


class Start:
    def __init__(self, root, scenario):
        self.scenario = scenario
        self.sim = Simulation(15, 15, 80, self.scenario)
        self.caretaker = ZapisStanow(self.sim)

        root.configure(bg="#FFC0CB")  # Różowe tło

        self.canvas = FigureCanvasTkAgg(self.sim.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        panel_przyciskow = tk.Frame(root, bg="#FFC0CB")
        panel_przyciskow.pack(side=tk.BOTTOM, pady=10)

        # Przycisk "Zapisz stan"
        przycisk_zapisz = tk.Button(panel_przyciskow, text="Zapisz stan", command=self.zapisz, width=15, height=4,
                                    font=("Arial", 12), bg="#4CAF50", fg="white")
        przycisk_zapisz.pack(side=tk.LEFT, padx=5)

        # Przycisk "Przywróć stan"
        przycisk_przywroc = tk.Button(panel_przyciskow, text="Przywróć stan", command=self.przywroz, width=15,
                                      height=4, font=("Arial", 12), bg="#2196F3", fg="white")
        przycisk_przywroc.pack(side=tk.LEFT, padx=5)

        # Przycisk "Zatrzymaj symulację"
        przycisk_zatrzymaj = tk.Button(panel_przyciskow, text="Zatrzymaj symulację", command=self.zatrzymaj, width=15,
                                       height=4, font=("Arial", 12), bg="#FF5733", fg="white")
        przycisk_zatrzymaj.pack(side=tk.LEFT, padx=5)

        # Przycisk "Wznów symulację"
        przycisk_wznów = tk.Button(panel_przyciskow, text="Wznów symulację", command=self.wznow, width=15, height=4,
                                   font=("Arial", 12), bg="#33FF57", fg="white")
        przycisk_wznów.pack(side=tk.LEFT, padx=5)

        # Przycisk "Zapisz jako obraz"
        przycisk_zapisz_plik = tk.Button(panel_przyciskow, text="Zapisz jako obraz", command=self.zapisz_jako_plik,
                                         width=20, height=4, font=("Arial", 12), bg="#FFD700", fg="black")
        przycisk_zapisz_plik.pack(side=tk.LEFT, padx=5)

        # Animacja
        self.ani = FuncAnimation(
            self.sim.fig, self.sim.update, frames=np.arange(0, 1000, 1),
            init_func=self.sim.init, blit=False, interval=40
        )
        self.canvas.draw()

        root.protocol("WM_DELETE_WINDOW", self.zamknij)

    def zamknij(self):
        """Obsługuje zamknięcie aplikacji."""
        if self.ani.event_source:
            self.ani.event_source.stop()

        self.sim.fig.clear()
        print("Symulacja została zamknięta.")
        sys.exit(0)

    def zapisz(self):
        """Zapisuje stan symulacji."""
        self.caretaker.save()
        print("Zapisano stan!")

    def przywroz(self):
        """Przywraca zapisany stan symulacji."""
        if self.caretaker.mementos:
            try:
                index = int(input(f"Wpisz numer zapisu (1 do {len(self.caretaker.mementos)}): "))
                if 1 <= index <= len(self.caretaker.mementos):
                    self.caretaker.restore(index - 1)
                    self.sim.scatter.set_offsets(np.empty((0, 2)))  # Reset cząsteczek
                    self.sim.init()  # Ponowne inicjalizowanie
                    print(f"Przywrócono zapis nr {index}!")
                else:
                    print("Nieprawidłowy numer zapisu.")
            except ValueError:
                print("Podaj liczbę całkowitą.")
        else:
            print("Brak zapisanych stanów.")

    def zatrzymaj(self):
        """Zatrzymuje symulację."""
        if self.ani.event_source:
            self.ani.event_source.stop()
            print("Symulacja została zatrzymana.")

    def wznow(self):
        """Wznawia symulację."""
        if self.ani.event_source:
            self.ani.event_source.start()
            print("Symulacja została wznowiona.")

    def zapisz_jako_plik(self):
        """Zapisuje aktualny wykres jako obraz do pliku."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file_path:
            try:
                self.sim.fig.savefig(file_path, bbox_inches="tight")
                print(f"Zapisano symulację jako obraz: {file_path}")
            except Exception as e:
                print(f"Błąd podczas zapisywania obrazu: {e}")


if __name__ == "__main__":
    print("Wybierz scenariusz:")
    print("1 - Wersja 1 ")
    print("2 - Wersja 2 ")

    try:
        ver = int(input("Podaj numer scenariusza (1 lub 2): "))
        if ver not in [1, 2]:
            raise ValueError("Nieprawidłowy numer scenariusza.")
    except ValueError as e:
        print(f"Błąd: {e}. Zamykam program.")
        sys.exit(0)

    root = tk.Tk()

    app = Start(root, ver)
    root.mainloop()
