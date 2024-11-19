import random

class MonteCarloPiEstimator:
    def __init__(self, n_points):
        # Inizializza il numero di punti da simulare
        self.n_points = n_points
        self.points_in_circle = 0

    def simulate(self):
        # Simula i punti casuali e conta quelli all'interno del cerchio
        self.points_in_circle = 0
        for _ in range(self.n_points):
            x, y = random.uniform(-1, 1), random.uniform(-1, 1)
            if x**2 + y**2 <= 1:
                self.points_in_circle += 1

    def estimate_pi(self):
        # Calcola il valore stimato di π
        return 4 * (self.points_in_circle / self.n_points)

    def print_results(self):
        # Stampa il risultato della simulazione
        estimated_pi = self.estimate_pi()
        print(f"Numero di punti simulati: {self.n_points}")
        print(f"Punti all'interno del cerchio: {self.points_in_circle}")
        print(f"Valore stimato di π: {estimated_pi:.4f}")

if __name__ == "__main__":
    # Chiede all'utente il numero di punti da simulare
    n_points = int(input("Inserisci il numero di punti da simulare: "))
    
    estimator = MonteCarloPiEstimator(n_points)
    estimator.simulate()  # Esegue la simulazione
    estimator.print_results()  # Stampa i risultati
