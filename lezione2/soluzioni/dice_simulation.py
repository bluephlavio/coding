import random
import statistics

class DiceSimulator:
    def __init__(self, rolls):
        # Inizializza il numero di lanci del dado
        self.rolls = rolls
        self.results = []

    def simulate(self):
        # Simula i lanci del dado
        self.results = [random.randint(1, 6) for _ in range(self.rolls)]

    def get_occurrences(self):
        # Restituisce le frequenze di ciascun numero
        return {i: self.results.count(i) for i in range(1, 7)}

    def get_mean(self):
        # Restituisce la media dei risultati
        return statistics.mean(self.results)

    def get_std_dev(self):
        # Restituisce la deviazione standard dei risultati
        return statistics.stdev(self.results)

    def print_occurrences(self):
        # Stampa le occorrenze di ciascun numero
        occurrences = self.get_occurrences()
        for number, count in occurrences.items():
            print(f"Occorrenze {number}: {count} volte")

    def print_statistics(self):
        # Stampa la media e la deviazione standard
        mean = self.get_mean()
        std_dev = self.get_std_dev()
        print(f"Media: {mean:.2f}")
        print(f"Deviazione standard: {std_dev:.2f}")

if __name__ == "__main__":
    # Chiede all'utente quanti lanci del dado simulare
    rolls = int(input("Quanti lanci vuoi simulare? "))
    
    simulator = DiceSimulator(rolls)
    simulator.simulate()  # Simula i lanci
    
    # Stampa i risultati utilizzando i metodi dedicati
    simulator.print_occurrences()
    simulator.print_statistics()
